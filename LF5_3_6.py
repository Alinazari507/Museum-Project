import json
from datetime import datetime

# --- 1. Domain Layer (The Core Logic) ---

class Dimensions:
    """Value Object: Defined only by its attributes (immutable logic)."""
    def __init__(self, height_cm: float, width_cm: float, depth_cm: float):
        # Validation is handled by setters
        self.height_cm = height_cm
        self.width_cm = width_cm
        self.depth_cm = depth_cm

    @property
    def height_cm(self): return self._height_cm
    @height_cm.setter
    def height_cm(self, value):
        if value <= 0: raise ValueError("Height must be positive.")
        self._height_cm = value

    @property
    def width_cm(self): return self._width_cm
    @width_cm.setter
    def width_cm(self, value):
        if value <= 0: raise ValueError("Width must be positive.")
        self._width_cm = value

    @property
    def depth_cm(self): return self._depth_cm
    @depth_cm.setter
    def depth_cm(self, value):
        if value <= 0: raise ValueError("Depth must be positive.")
        self._depth_cm = value

    def __str__(self):
        return f"{self.height_cm}x{self.width_cm}x{self.depth_cm} cm"


class Exhibit:
    """Entity: Has a unique identity (exhibit_id)."""
    def __init__(self, exhibit_id: str, title: str, artist: str, year: int, dimensions: Dimensions, description=""):
        self.exhibit_id = exhibit_id
        self.title = title
        self.artist = artist
        self.year = year  # Triggers validation
        self.dimensions = dimensions
        self.description = description

    @property
    def year(self): return self._year
    @year.setter
    def year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise ValueError(f"Year {value} cannot be in the future.")
        self._year = value

    def to_dict(self):
        """Prepares data for JSON serialization."""
        return {
            "exhibit_id": self.exhibit_id,
            "title": self.title,
            "artist": self.artist,
            "year": self.year,
            "description": self.description,
            "dimensions": {
                "height": self.dimensions.height_cm,
                "width": self.dimensions.width_cm,
                "depth": self.dimensions.depth_cm
            }
        }

# --- 2. Infrastructure Layer (Data Persistence) ---

def save_exhibits_to_json(exhibit_list, filename="museum.json"):
    """Converts objects to dicts and saves to a file."""
    try:
        data = [exhibit.to_dict() for exhibit in exhibit_list]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"✅ Data saved successfully to {filename}")
    except Exception as e:
        print(f"❌ Storage Error: {e}")

def find_exhibit_by_artist(filename, artist_name):
    """Business Logic: Search filter for the collection."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            all_data = json.load(f)
        return [e for e in all_data if artist_name.lower() in e['artist'].lower()]
    except FileNotFoundError:
        print("⚠️ Database file not found.")
        return []

# --- 3. Execution (Testing the Story) ---

if __name__ == "__main__":
    try:
        # Create Objects
        d1 = Dimensions(120, 90, 5)
        exhibit1 = Exhibit("ART-001", "Starry Night", "Van Gogh", 1889, d1, "Oil painting")

        d2 = Dimensions(200, 100, 100)
        exhibit2 = Exhibit("ART-002", "David", "Michelangelo", 1504, d2, "Marble sculpture")

        # Save to JSON
        my_collection = [exhibit1, exhibit2]
        save_exhibits_to_json(my_collection)

        # Search and Display
        print("\n🔎 Searching for 'Van Gogh'...")
        search_results = find_exhibit_by_artist("museum.json", "Van Gogh")
        for item in search_results:
            print(f"Found: {item['title']} ({item['year']}) - ID: {item['exhibit_id']}")

    except ValueError as e:
        print(f"⚠️ Validation Error: {e}")