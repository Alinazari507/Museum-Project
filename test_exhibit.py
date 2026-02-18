import unittest
from your_filename import Dimensions, Exhibit # replace 'your_filename' with your actual file name

class TestMuseumProject(unittest.TestCase):
    
    def test_dimensions_valid(self):
        """Test if valid dimensions are accepted."""
        dims = Dimensions(100, 50, 10)
        self.assertEqual(dims.height_cm, 100)

    def test_dimensions_invalid(self):
        """Test if negative dimensions raise ValueError."""
        with self.assertRaises(ValueError):
            Dimensions(-10, 50, 10)

    def test_future_year(self):
        """Test if a future year raises ValueError in Exhibit."""
        dims = Dimensions(10, 10, 10)
        with self.assertRaises(ValueError):
            Exhibit("ID-1", "Future Art", "Artist", 2099, dims)

if __name__ == "__main__":
    unittest.main()