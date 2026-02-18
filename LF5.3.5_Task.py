class Artist:
    def __init__(self, name, birth_year, id_number, style):
        # Public Attributes (State)
        self.name = name
        self.birth_year = birth_year
        self.style = style

        # Private State: Using the _ prefix as per mandatory tasks
        self._internal_id = id_number

    # Method (Behavior): Calculates age based on a given year
    def calculate_age(self, current_year):
        return current_year - self.birth_year

    # Public Method: To safely view the internal ID (Encapsulation)
    def get_id(self):
        return self._internal_id

# Instantiate: Creating two unique objects
artist1 = Artist("Leonardo da Vinci", 1452, "ART001", "High Renaissance")
artist2 = Artist("Pablo Picasso", 1881, "ART002", "Cubism")

# Testing the objects and methods
print(f"Name: {artist1.name} | ID: {artist1.get_id()} | Style: {artist1.style}")
print(f"Age in 2026: {artist1.calculate_age(2026)}")
print("-" * 30)
print(f"Name: {artist2.name} | ID: {artist2.get_id()} | Style: {artist2.style}")
print(f"Age in 2026: {artist2.calculate_age(2026)}")