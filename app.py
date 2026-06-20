import os
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="🎬 Netflix Catalog Analyzer",
    page_icon="🍿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .reportview-container {
        background: #141414;
    }
    .main-header {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #E50914;
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 20px;
    }
    .sub-header {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #f5f5f1;
        font-size: 16px;
        text-align: center;
        margin-bottom: 40px;
    }
    .metric-card {
        background-color: #1f1f1f;
        border: 1px solid #333333;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    .metric-val {
        color: #E50914;
        font-size: 32px;
        font-weight: 800;
    }
    .metric-lbl {
        color: #b3b3b3;
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
</style>
""", unsafe_allowed_html=True)

# Data Loading (Cached for performance)
@st.cache_data
def load_data():
    csv_path = os.path.join(os.path.dirname(__file__), 'data', 'netflix.csv')
    df = pd.read_csv(csv_path)
    
    # Preprocessing
    df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), format="mixed", errors="coerce")
    df["year_added"] = df["date_added"].dt.year.astype("Int64")
    df["month_added"] = df["date_added"].dt.month.astype("Int64")
    df["month_name"] = df["date_added"].dt.month_name()
    
    # Impute missing values
    fill_map = {
        "director": "Unknown",
        "cast": "Unknown",
        "country": "Unknown",
        "rating": "Unrated",
    }
    for col, val in fill_map.items():
        df[col] = df[col].fillna(val)
        
    # Parse duration
    df["duration_int"] = df["duration"].str.extract(r"(\d+)").astype(float)
    df["duration_unit"] = df["duration"].str.extract(r"(min|Season)")
    
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading netflix.csv: {e}")
    st.stop()

# Helper for list unnesting (Unique values extraction)
@st.cache_data
def get_unique_elements(series):
    elements = series.dropna().str.split(", ").explode().str.strip()
    return sorted(elements.unique())

unique_countries = get_unique_elements(df["country"])
unique_genres = get_unique_elements(df["listed_in"])

# ── Sidebar Filter Setup ──────────────────────────────────────────────────
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg", width=180)
st.sidebar.markdown("<br>", unsafe_allowed_html=True)
st.sidebar.title("🔍 Search Filters")

# 1. Content Type Filter
content_type = st.sidebar.radio("Content Type", ["All", "Movie", "TV Show"])

# 2. Release Year Filter
min_year = int(df["release_year"].min())
max_year = int(df["release_year"].max())
selected_years = st.sidebar.slider("Release Year Range", min_year, max_year, (2000, max_year))

# 3. Country Filter
selected_countries = st.sidebar.multiselect("Select Countries (Default: All)", unique_countries)

# 4. Genre Filter
selected_genres = st.sidebar.multiselect("Select Genres (Default: All)", unique_genres)

# Apply filters
df_filtered = df.copy()

# Year filtering
df_filtered = df_filtered[
    (df_filtered["release_year"] >= selected_years[0]) & 
    (df_filtered["release_year"] <= selected_years[1])
]

# Type filtering
if content_type != "All":
    df_filtered = df_filtered[df_filtered["type"] == content_type]

# Country filtering
if selected_countries:
    mask_country = df_filtered['country'].apply(
        lambda x: any(c.strip() in [s.strip() for s in str(x).split(',')] for c in selected_countries)
    )
    df_filtered = df_filtered[mask_country]

# Genre filtering
if selected_genres:
    mask_genre = df_filtered['listed_in'].apply(
        lambda x: any(g.strip() in [s.strip() for s in str(x).split(',')] for g in selected_genres)
    )
    df_filtered = df_filtered[mask_genre]

# Page Header
st.markdown("<div class='main-header'>🎬 Netflix Catalog Analyzer</div>", unsafe_allowed_html=True)
st.markdown("<div class='sub-header'>Interactive business intelligence tool for content acquisition and strategy</div>", unsafe_allowed_html=True)

# ── KPI Cards ─────────────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-val'>{len(df_filtered):,}</div>
        <div class='metric-lbl'>Total Titles</div>
    </div>
    """, unsafe_allowed_html=True)

with col2:
    movies_count = len(df_filtered[df_filtered["type"] == "Movie"])
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-val'>{movies_count:,}</div>
        <div class='metric-lbl'>Movies Count</div>
    </div>
    """, unsafe_allowed_html=True)

with col3:
    shows_count = len(df_filtered[df_filtered["type"] == "TV Show"])
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-val'>{shows_count:,}</div>
        <div class='metric-lbl'>TV Shows Count</div>
    </div>
    """, unsafe_allowed_html=True)

with col4:
    # Most active country in filtered dataset
    active_countries = df_filtered["country"].str.split(", ").explode().str.strip()
    active_countries = active_countries[active_countries != "Unknown"]
    top_country = active_countries.mode()[0] if not active_countries.empty else "N/A"
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-val'>{top_country}</div>
        <div class='metric-lbl'>Top Producer</div>
    </div>
    """, unsafe_allowed_html=True)

st.markdown("<br><br>", unsafe_allowed_html=True)

# ── Visualizations Grid ───────────────────────────────────────────────────
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("📊 Catalog Composition (Movies vs TV Shows)")
    type_counts = df_filtered["type"].value_counts().reset_index()
    type_counts.columns = ["Type", "Count"]
    fig_pie = px.pie(
        type_counts, 
        values="Count", 
        names="Type", 
        hole=0.5, 
        color_discrete_sequence=["#E50914", "#303030"],
        template="plotly_dark"
    )
    fig_pie.update_layout(margin=dict(t=20, b=20, l=20, r=20), height=350)
    st.plotly_chart(fig_pie, use_container_width=True)

with row1_col2:
    st.subheader("📈 Content Additions Over Time")
    growth_df = df_filtered.groupby(["year_added", "type"]).size().reset_index(name="count")
    fig_growth = px.line(
        growth_df, 
        x="year_added", 
        y="count", 
        color="type",
        markers=True,
        color_discrete_sequence=["#E50914", "#b3b3b3"],
        template="plotly_dark"
    )
    fig_growth.update_layout(
        xaxis_title="Year Added", 
        yaxis_title="Titles Added",
        legend_title="Type",
        margin=dict(t=20, b=20, l=20, r=20),
        height=350
    )
    st.plotly_chart(fig_growth, use_container_width=True)

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("🎭 Top Genres (Exploded)")
    genres_series = df_filtered["listed_in"].str.split(", ").explode().str.strip()
    genres_df = genres_series.value_counts().head(10).reset_index()
    genres_df.columns = ["Genre", "Count"]
    
    fig_genre = px.bar(
        genres_df,
        y="Genre",
        x="Count",
        orientation="h",
        color_discrete_sequence=["#E50914"],
        template="plotly_dark"
    )
    fig_genre.update_layout(
        yaxis=dict(autorange="reversed"),
        xaxis_title="Catalog Count",
        margin=dict(t=20, b=20, l=20, r=20),
        height=380
    )
    st.plotly_chart(fig_genre, use_container_width=True)

with row2_col2:
    st.subheader("🌎 Top Producing Countries (Exploded)")
    countries_series = df_filtered["country"].str.split(", ").explode().str.strip()
    countries_series = countries_series[countries_series != "Unknown"]
    countries_df = countries_series.value_counts().head(10).reset_index()
    countries_df.columns = ["Country", "Count"]
    
    fig_country = px.bar(
        countries_df,
        y="Country",
        x="Count",
        orientation="h",
        color_discrete_sequence=["#564d4d"],
        template="plotly_dark"
    )
    fig_country.update_layout(
        yaxis=dict(autorange="reversed"),
        xaxis_title="Catalog Count",
        margin=dict(t=20, b=20, l=20, r=20),
        height=380
    )
    st.plotly_chart(fig_country, use_container_width=True)

# ── Durations Analysis ────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allowed_html=True)
st.subheader("⏱️ Content Duration Distribution Analysis")
dur_col1, dur_col2 = st.columns(2)

with dur_col1:
    st.markdown("##### Movies Running Time (Minutes)")
    movies_dur = df_filtered[(df_filtered["type"] == "Movie") & (df_filtered["duration_unit"] == "min")]
    if not movies_dur.empty:
        fig_movies_hist = px.histogram(
            movies_dur,
            x="duration_int",
            nbins=35,
            color_discrete_sequence=["#E50914"],
            template="plotly_dark",
            labels={"duration_int": "Running Time (mins)"}
        )
        fig_movies_hist.update_layout(margin=dict(t=10, b=20, l=20, r=20), height=300)
        st.plotly_chart(fig_movies_hist, use_container_width=True)
    else:
        st.info("No Movie data matches current filter settings.")

with dur_col2:
    st.markdown("##### TV Shows Length (Seasons)")
    shows_dur = df_filtered[(df_filtered["type"] == "TV Show") & (df_filtered["duration_unit"] == "Season")]
    if not shows_dur.empty:
        fig_shows_hist = px.histogram(
            shows_dur,
            x="duration_int",
            nbins=10,
            color_discrete_sequence=["#564d4d"],
            template="plotly_dark",
            labels={"duration_int": "Total Seasons"}
        )
        fig_shows_hist.update_layout(margin=dict(t=10, b=20, l=20, r=20), height=300)
        st.plotly_chart(fig_shows_hist, use_container_width=True)
    else:
        st.info("No TV Show data matches current filter settings.")

# ── Interactive Data Explorer ─────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allowed_html=True)
with st.expander("📂 Interactive Data Explorer & Catalog Search"):
    st.write(f"Displaying **{len(df_filtered):,}** records based on active filters.")
    
    # Selection of display columns
    display_cols = ["show_id", "type", "title", "director", "cast", "country", "release_year", "rating", "duration", "listed_in"]
    st.dataframe(df_filtered[display_cols], use_container_width=True)
    
    # Download Button
    csv = df_filtered[display_cols].to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv,
        file_name="netflix_filtered_catalog.csv",
        mime="text/csv",
    )

# ── Strategic Insights Expander ───────────────────────────────────────────
st.markdown("<br>", unsafe_allowed_html=True)
with st.expander("💡 Strategic Business Recommendations & Key Insights"):
    st.markdown("""
    ### Key Business Insights
    1. **Primary Focus (Movies vs TV Shows)**: Movies account for over 69% of the catalog, but TV Shows have seen massive growth in acquisition rate. TV Shows increase retention/watch time, while Movies provide immediate customer pull.
    2. **Dominant Genres**: *Dramas*, *Comedies*, and *International Movies* represent the largest genre groupings on Netflix. International expansion requires localization of these genres.
    3. **Regional Hubs**: The **United States**, **India**, and the **United Kingdom** are the top three content hubs. India leads the South Asian production sector.
    4. **Optimal Timing**: Launch volumes peak around **November** and **December** (holiday periods) and **July** (summer holiday). Launching content during these months aligns with peak subscriber watch-time.
    
    ### Actionable Recommendations
    - **Prioritize TV Shows Production**: Continue scaling up original TV Show productions, especially in high-growth international markets to sustain customer subscription cycles.
    - **Expand Regional Localization**: Invest heavily in local language content (especially Dramas and Comedies) in fast-growing regions like Latin America and Southeast Asia.
    - **Align Content Launches**: Plan original flagship releases during November/December holiday season to capture the maximum audience share.
    """)
