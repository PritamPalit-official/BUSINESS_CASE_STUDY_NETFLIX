import unittest

def parse_multiple_values(val_str):
    """Reflected logic: converts comma separated list (cast/directors) into lists."""
    if not val_str:
        return []
    return [v.strip() for v in val_str.split(',')]

def categorize_duration(duration_str):
    """Reflected logic: classifies duration into categories."""
    if not duration_str:
        return "Unknown"
    if "Season" in duration_str:
        return "TV Show"
    try:
        minutes = int(duration_str.split()[0])
        if minutes < 90:
            return "Short Movie"
        elif minutes <= 130:
            return "Standard Movie"
        return "Long Movie"
    except ValueError:
        return "Unknown"

class TestNetflixPipeline(unittest.TestCase):
    def test_parse_multiple_values(self):
        self.assertEqual(parse_multiple_values("David Attenborough, Alastair Fothergill"), ["David Attenborough", "Alastair Fothergill"])
        self.assertEqual(parse_multiple_values(""), [])
        
    def test_categorize_duration(self):
        self.assertEqual(categorize_duration("1 Season"), "TV Show")
        self.assertEqual(categorize_duration("85 min"), "Short Movie")
        self.assertEqual(categorize_duration("110 min"), "Standard Movie")
        self.assertEqual(categorize_duration("150 min"), "Long Movie")
        self.assertEqual(categorize_duration(""), "Unknown")

if __name__ == '__main__':
    unittest.main()
