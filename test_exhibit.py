import unittest
from LF5_3_6 import Dimensions, Exhibit # Ensure the filename matches your script

class TestMuseumSystem(unittest.TestCase):

    def setUp(self):
        """Set up a fresh exhibit for each test."""
        self.valid_dims = Dimensions(100, 50, 10)
        self.exhibit = Exhibit("TEST-01", "Mona Lisa", "Da Vinci", 1503, self.valid_dims)

    def test_valid_creation(self):
        """Test if the exhibit is created with correct data."""
        self.assertEqual(self.exhibit.title, "Mona Lisa")
        self.assertEqual(self.exhibit.dimensions.height_cm, 100)

    def test_invalid_dimensions(self):
        """Test if negative dimensions raise a ValueError."""
        with self.assertRaises(ValueError):
            Dimensions(-10, 50, 5)

    def test_future_year(self):
        """Test if a future year raises a ValueError."""
        with self.assertRaises(ValueError):
            self.exhibit.year = 2099

    def test_json_conversion(self):
        """Test if the to_dict method produces the correct dictionary structure."""
        data = self.exhibit.to_dict()
        self.assertEqual(data["exhibit_id"], "TEST-01")
        self.assertIn("dimensions", data)
        self.assertEqual(data["dimensions"]["height"], 100)

if __name__ == "__main__":
    unittest.main()