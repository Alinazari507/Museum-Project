import json
from datetime import datetime

# --- Domain Layer ---

class Dimensions:
    """Handles physical dimensions with validation."""
    def __init__(self, height_cm, width_cm, depth_cm):
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

class Exhibit:
    """Manages museum exhibits including ID, title, artist, year, dimensions, and description."""
    def __init__(self, exhibit_id, title, artist, year, dimensions: Dimensions, description=""):
        self.exhibit_id = exhibit_id
        self.title = title
        self.artist = artist
        self.year = year  # Triggers setter validation
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
        """Converts exhibit data to a dictionary for JSON storage."""
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

# --- Infrastructure Layer ---

def save_exhibits_to_json(exhibit_list, filename="museum.json"):
    """Saves a list of exhibit objects to a JSON file."""
    try:
        data = [exhibit.to_dict() for exhibit in exhibit_list]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"✅ Success: Saved {len(exhibit_list)} items to {filename}")
    except Exception as e:
        print(f"❌ Error: Could not save data: {e}")

def find_exhibit_by_artist(filename, artist_name):
    """Searches for exhibits by artist name in the JSON database."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            all_data = json.load(f)
        results = [e for e in all_data if artist_name.lower() in e['artist'].lower()]
        return results
    except FileNotFoundError:
        return []

# --- Main Application Logic ---

if __name__ == "__main__":
    try:
        # 1. Initialize Dimensions
        dims1 = Dimensions(120, 90, 5)
        dims2 = Dimensions(200, 100, 100)

        # 2. Initialize Exhibits (with descriptions)
        exhibit1 = Exhibit(
            "ART-001", "Starry Night", "Van Gogh", 1889, dims1, 
            "Famous oil-on-canvas painting showing a night view."
        )
        exhibit2 = Exhibit(
            "ART-002", "David", "Michelangelo", 1504, dims2, 
            "A masterpiece of Renaissance sculpture created in marble."
        )

        # 3. Storage
        museum_collection = [exhibit1, exhibit2]
        save_exhibits_to_json(museum_collection)

        # 4. Search Verification
        print("\n🔎 Searching for 'Michelangelo':")
        results = find_exhibit_by_artist("museum.json", "Michelangelo")
        for item in results:
            print(f"ID: {item['exhibit_id']} | Title: {item['title']} | Info: {item['description']}")

    except ValueError as e:
        print(f"⚠️ Data Error: {e}")