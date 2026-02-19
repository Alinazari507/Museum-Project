import json
from functools import reduce
from LF5_3_models import Exhibit, Dimensions 

class ExhibitRepository:
    def __init__(self, filename="exhibits.json"):
        self._exhibits = []
        self.filename = filename

    def add(self, exhibit: Exhibit):
        """Adds a new exhibit object to the internal collection."""
        self._exhibits.append(exhibit)

    def get_all(self):
        """Returns the full list of exhibit objects."""
        return self._exhibits

    # --- ADVANCED QUERY ENGINE (The Epic Addition) ---

    def query(self, filter_logic):
        """
        Advanced Query: Accepts a lambda function to filter exhibits.
        Example: repo.query(lambda e: e.year < 1900)
        """
        return list(filter(filter_logic, self._exhibits))

    def calculate_average_year(self):
        """
        Uses Map and Reduce to calculate the average age of exhibits.
        Demonstrates Functional Programming from Lesson 8.
        """
        if not self._exhibits:
            return 0
        
        # 1. Map: Extract only the years
        years = list(map(lambda e: e.year, self._exhibits))
        
        # 2. Reduce: Sum all years
        total_years = reduce(lambda x, y: x + y, years)
        
        return total_years / len(years)

    # --- PERSISTENCE LAYER (JSON Handling) ---

    def save_to_json(self):
        """Saves current exhibits to a JSON file with professional formatting."""
        data_to_save = []
        for e in self._exhibits:
            ex_dict = {
                "id": e.exhibit_id,
                "title": e.title,
                "artist": e.artist,
                "year": e.year,
                "dimensions": {
                    "h": e.dimensions.height_cm,
                    "w": e.dimensions.width_cm,
                    "d": e.dimensions.depth_cm
                }
            }
            data_to_save.append(ex_dict)
        
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(data_to_save, f, indent=4, ensure_ascii=False)
            print(f"✅ Data successfully saved to {self.filename}")
        except Exception as e:
            print(f"❌ Storage Error: {e}")

    def load_from_json(self):
        """Loads data and reconstructs Exhibit and Dimensions objects."""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self._exhibits = [] 
                for item in data:
                    # Reconstructing Value Object (Dimensions)
                    dims = Dimensions(
                        item["dimensions"]["h"], 
                        item["dimensions"]["w"], 
                        item["dimensions"]["d"]
                    )
                    # Reconstructing Entity (Exhibit)
                    exhibit = Exhibit(
                        item["id"], 
                        item["title"], 
                        item["artist"], 
                        item["year"], 
                        dims
                    )
                    self._exhibits.append(exhibit)
            print(f"✅ Successfully loaded {len(self._exhibits)} exhibits.")
        except FileNotFoundError:
            print("⚠️ No database found. Starting fresh.")
        except Exception as e:
            print(f"❌ Load Error: {e}")