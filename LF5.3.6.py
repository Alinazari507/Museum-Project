import json
from datetime import datetime

class Dimensions:
    """Represents the physical size of an object as a Value Object."""
    def __init__(self, height_cm, width_cm, depth_cm):
        # Using setters to ensure data integrity from the start
        self.height_cm = height_cm
        self.width_cm = width_cm
        self.depth_cm = depth_cm

    @property
    def height_cm(self):
        return self._height_cm

    @height_cm.setter
    def height_cm(self, value):
        if value <= 0:
            raise ValueError("Height must be a positive number.")
        self._height_cm = value

    @property
    def width_cm(self):
        return self._width_cm

    @width_cm.setter
    def width_cm(self, value):
        if value <= 0:
            raise ValueError("Width must be a positive number.")
        self._width_cm = value

    @property
    def depth_cm(self):
        return self._depth_cm

    @depth_cm.setter
    def depth_cm(self, value):
        if value <= 0:
            raise ValueError("Depth must be a positive number.")
        self._depth_cm = value

    def __eq__(self, other):
        if not isinstance(other, Dimensions):
            return False
        return (self.height_cm == other.height_cm and
                self.width_cm == other.width_cm and
                self.depth_cm == other.depth_cm)


class Exhibit:
    """Represents a museum exhibit as an Entity."""
    def __init__(self, exhibit_id, title, artist, year, dimensions: Dimensions):
        self.exhibit_id = exhibit_id
        self.title = title
        self.artist = artist
        self.year = year # This triggers the setter validation
        self.dimensions = dimensions

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise ValueError(f"Year {value} cannot be in the future.")
        self._year = value

    def to_dict(self):
        """Standardizes the object for JSON export."""
        return {
            "exhibit_id": self.exhibit_id,
            "title": self.title,
            "artist": self.artist,
            "year": self.year,
            "dimensions": {
                "height": self.dimensions.height_cm,
                "width": self.dimensions.width_cm,
                "depth": self.dimensions.depth_cm
            }
        }

    def __eq__(self, other):
        if not isinstance(other, Exhibit):
            return False
        return self.exhibit_id == other.exhibit_id


# --- Management Tools (Owner Functions) ---

def save_to_json(exhibit_list, filename="museum.json"):
    """Saves a list of exhibits to a JSON file."""
    try:
        data_to_save = [exhibit.to_dict() for exhibit in exhibit_list]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, indent=4, ensure_ascii=False)
        print(f"Successfully saved {len(exhibit_list)} items to {filename}")
    except Exception as e:
        print(f"Critical Error saving to file: {e}")


# --- Main Execution (Testing the entire system) ---

if __name__ == "__main__":
    try:
        # 1. Create dimensions
        painting_dims = Dimensions(120, 90, 5)
        statue_dims = Dimensions(200, 100, 100)

        # 2. Create Exhibits
        exhibit1 = Exhibit("ART-101", "Starry Night", "Van Gogh", 1889, painting_dims)
        exhibit2 = Exhibit("ART-102", "David", "Michelangelo", 1504, statue_dims)

        # 3. Put them in a list (The collection)
        my_museum_collection = [exhibit1, exhibit2]

        # 4. Show initial details
        print(f"Managing {len(my_museum_collection)} exhibits.")
        
        # 5. Save all to JSON
        save_to_json(my_museum_collection)

        # 6. Test Validation (Try changing to a future year - will fail)
        # exhibit1.year = 2050 

    except ValueError as error:
        print(f"Validation failed: {error}")