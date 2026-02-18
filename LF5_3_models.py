class Dimensions:
    def __init__(self, height_cm: float, width_cm: float, depth_cm: float):
        self.height_cm = height_cm
        self.width_cm = width_cm
        self.depth_cm = depth_cm

    def __repr__(self):
        return f"{self.height_cm}x{self.width_cm}x{self.depth_cm} cm"

class Exhibit:
    def __init__(self, exhibit_id: str, title: str, artist: str, year: int, dimensions: Dimensions):
        self.exhibit_id = exhibit_id
        self.title = title
        self.artist = artist
        self.year = year
        self.dimensions = dimensions

    def update_title(self, new_title: str):
        self.title = new_title

    def __str__(self):
        return f"[{self.exhibit_id}] {self.title} by {self.artist} ({self.year})"