import unittest
from LF5_3_models import Exhibit, Dimensions

class TestMuseumProject(unittest.TestCase):
    def setUp(self):
        self.dims = Dimensions(100.0, 80.0, 5.0)
        self.exhibit = Exhibit("MUSE-001", "Starry Night", "Van Gogh", 1889, self.dims)

    def test_exhibit_identity(self):
        """Check if exhibit ID is assigned correctly"""
        self.assertEqual(self.exhibit.exhibit_id, "MUSE-001")

    def test_dimensions_value(self):
        """Check if dimensions are stored as a value object"""
        self.assertEqual(self.exhibit.dimensions.height_cm, 100.0)

    def test_invalid_dimensions(self):
        """Test if negative dimensions raise an error (K6 Evaluation)"""
        with self.assertRaises(ValueError):
            Dimensions(-10, 20, 30)

if __name__ == '__main__':
    unittest.main()