# LF5_3_repository.py
import json
from LF5_3_models import Exhibit, Dimensions 

class ExhibitRepository:
    def __init__(self, filename="exhibits.json"):
        self._exhibits = []
        self.filename = filename

    def add(self, exhibit: Exhibit):
        self._exhibits.append(exhibit)

    def get_all(self):
        """Returns the list of all exhibits"""
        return self._exhibits

    def save_to_json(self):
        """Saves current exhibits to a JSON file"""
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
        
        with open(self.filename, "w") as f:
            json.dump(data_to_save, f, indent=4)
        print(f"Data successfully saved to {self.filename}")

    def load_from_json(self):
        """Loads exhibits from the JSON file"""
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self._exhibits = [] 
                for item in data:
                    dims = Dimensions(
                        item["dimensions"]["h"], 
                        item["dimensions"]["w"], 
                        item["dimensions"]["d"]
                    )
                    exhibit = Exhibit(
                        item["id"], 
                        item["title"], 
                        item["artist"], 
                        item["year"], 
                        dims
                    )
                    self._exhibits.append(exhibit)
            print(f"Successfully loaded {len(self._exhibits)} exhibits.")
        except FileNotFoundError:
            print("No saved data found. Starting fresh.")