<div align="center">

# 🎬 Netflix Business Case Study

### Data Exploration & Business Insights on Netflix Content Strategy Across Countries

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-444876?style=for-the-badge&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<br/>

*A comprehensive, end-to-end exploratory & business-oriented data analysis on Netflix's global content catalog — uncovering patterns in content distribution, genre trends, regional strategies, and viewer preferences to derive actionable business recommendations.*

---

</div>

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [❓ Problem Statement](#-problem-statement)
- [📊 Dataset Description](#-dataset-description)
- [🔬 Analysis Performed](#-analysis-performed)
- [🛠️ Tools & Technologies](#️-tools--technologies)
- [📁 Project Structure](#-project-structure)
- [💡 Key Business Insights](#-key-business-insights)
- [📈 Recommendations](#-recommendations)
- [🚀 Getting Started](#-getting-started)
- [👤 Author](#-author)
- [📄 License](#-license)

---

## 🎯 Project Overview

This project presents an **end-to-end exploratory and business-oriented data analysis** on a Netflix content dataset. The objective is to analyze content distribution, trends, and user preferences — and to derive **actionable business insights** using Python-based data analysis and visualization techniques.

> **Why This Matters:** Netflix operates in 190+ countries and invests billions in content annually. Understanding what types of content perform well, which genres dominate, and where regional gaps exist is critical for strategic content planning and market expansion.

---

## ❓ Problem Statement

To understand **Netflix's content strategy** by analyzing:

- 🎭 **Content Types** — Movies vs. TV Shows distribution
- 🎬 **Genres** — Dominant and underrepresented categories
- ⭐ **Ratings** — Audience maturity segmentation
- 📅 **Release Patterns** — Temporal trends in content additions
- 🌍 **Country-wise Distribution** — Regional content concentration
- ⏱️ **Duration Characteristics** — Optimal content length ranges

…and to translate these findings into **strategic business recommendations**.

---

## 📊 Dataset Description

The dataset contains detailed information about **Movies and TV Shows** available on Netflix. Preprocessing steps were applied to handle missing values and transform categorical attributes.

### Dataset Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | `type` | Content type — Movie or TV Show |
| 2 | `title` | Name of the content |
| 3 | `director` | Director(s) of the content |
| 4 | `cast` | Lead actors / cast members |
| 5 | `country` | Country of origin / production |
| 6 | `release_year` | Year the content was originally released |
| 7 | `rating` | Content maturity rating (e.g., PG-13, TV-MA) |
| 8 | `listed_in` | Genre(s) / category of the content |
| 9 | `duration` | Length in minutes (Movies) or number of seasons (TV Shows) |

### Data Preprocessing

- ✅ Handled missing values across key columns (`director`, `cast`, `country`)
- ✅ Transformed categorical attributes for analysis compatibility
- ✅ Parsed and standardized duration fields for Movies and TV Shows

---

## 🔬 Analysis Performed

| Analysis Type | Techniques Used |
|---------------|----------------|
| **Exploratory Data Analysis (EDA)** | Shape inspection, data types, missing value audit, statistical summaries |
| **Non-Graphical Analysis** | Value counts, unique value enumeration, categorical frequency distributions |
| **Univariate Analysis** | Histograms, count plots, distribution curves for numerical variables |
| **Bivariate Analysis** | Boxplots, correlation heatmaps to study inter-variable relationships |
| **Outlier Detection** | IQR-based analysis specifically on movie duration |
| **Business Insights & Recommendations** | Data-driven strategic takeaways for content planning |

---

## 🛠️ Tools & Technologies

| Category | Tools |
|----------|-------|
| **Language** | Python 3.x |
| **Data Manipulation** | Pandas, NumPy |
| **Data Visualization** | Matplotlib, Seaborn |
| **Environment** | Jupyter Notebook |
| **Analysis Type** | Exploratory Data Analysis, Business Intelligence |

---

## 📁 Project Structure

```
BUSINESS_CASE_STUDY_NETFLIX/
│
├── 📄 README.md                          # Project documentation
├── 📑 BUSINESS_CASE_STUDY_NETFLIX.pdf    # Detailed analysis report with visualizations
```

> 📌 **Note:** The full analysis report — including all visualizations, code outputs, and business recommendations — is available in the [PDF report](BUSINESS_CASE_STUDY_NETFLIX.pdf).

---

## 💡 Key Business Insights

<table>
  <tr>
    <td>🎬</td>
    <td><b>Movies Dominate</b></td>
    <td>Netflix's catalog has a significantly higher proportion of movies compared to TV shows, indicating a content acquisition strategy skewed towards shorter-form content.</td>
  </tr>
  <tr>
    <td>🎭</td>
    <td><b>Genre Concentration</b></td>
    <td>Dramas and comedies dominate the genre landscape, revealing both market demand and a potential over-reliance on a limited set of categories.</td>
  </tr>
  <tr>
    <td>🌍</td>
    <td><b>Geographic Imbalance</b></td>
    <td>A small number of countries (primarily the US, India, and UK) contribute the vast majority of content, highlighting untapped regional markets.</td>
  </tr>
  <tr>
    <td>⏱️</td>
    <td><b>Duration Sweet Spots</b></td>
    <td>Content duration analysis reveals optimal ranges preferred by viewers — most movies cluster around 90–120 minutes, suggesting a viewer preference for standard-length films.</td>
  </tr>
  <tr>
    <td>⭐</td>
    <td><b>Rating Gaps</b></td>
    <td>The rating distribution reveals significant opportunities for expanding family-friendly (TV-Y, TV-G) and regionally targeted content.</td>
  </tr>
</table>

---

## 📈 Recommendations

| # | Recommendation | Strategic Impact |
|---|----------------|------------------|
| 1 | 📺 **Increase TV Show Production** | Improve long-term subscriber engagement and retention through multi-season content |
| 2 | 🌐 **Expand Regional Content** | Tap into underrepresented markets with localized, culturally relevant offerings |
| 3 | 🎭 **Diversify Genre Portfolio** | Reduce over-dependence on dramas & comedies; explore documentaries, thrillers, sci-fi |
| 4 | 🏷️ **Improve Metadata Quality** | Enhance content discoverability through better tagging, descriptions, and categorization |
| 5 | 📅 **Align Launches with Holidays** | Maximize viewership by timing major releases around global holiday seasons |

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.x installed along with the following libraries:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Run the Analysis

```bash
# Clone the repository
git clone https://github.com/PritamPalit-official/BUSINESS_CASE_STUDY_NETFLIX.git

# Navigate to the project directory
cd BUSINESS_CASE_STUDY_NETFLIX

# Open the PDF report
# Or launch Jupyter Notebook for interactive exploration
jupyter notebook
```

### Quick Start (Python)

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Netflix dataset
df = pd.read_csv("netflix_data.csv")

# Quick overview
print(f"Dataset Shape: {df.shape}")
print(f"Content Types:\n{df['type'].value_counts()}")

# Visualize content distribution
sns.countplot(data=df, x='type', palette='Set2')
plt.title('Netflix Content: Movies vs TV Shows')
plt.show()
```

---

## 👤 Author

<div align="center">

**Pritam Palit**

🎓 Electronics & Communication Engineering Graduate

📊 Focus Areas: Data Analytics | Statistics | Business Intelligence

[![GitHub](https://img.shields.io/badge/GitHub-PritamPalit--official-181717?style=for-the-badge&logo=github)](https://github.com/PritamPalit-official)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Pritam_Palit-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/pritam-palit-77b2071b4/)

</div>

---

## 📄 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute this project with proper attribution.

```
MIT License

Copyright (c) 2025 Pritam Palit

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

<div align="center">

⭐ **If you found this project useful, consider giving it a star!** ⭐

*Built with 💡 data-driven thinking and ❤️ by [Pritam Palit](https://github.com/PritamPalit-official)*

</div>
