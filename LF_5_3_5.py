from datetime import datetime

# -------------------------------
# 1️⃣ Base Class (Parent Class) - Generalization
# -------------------------------
class Person:
    def __init__(self, name: str, birth_year: int, id_number: str):
        self.name = name
        self.birth_year = birth_year
        self._internal_id = id_number  # Encapsulation: Private attribute

    def calculate_age(self) -> int:
        """Calculates age based on the current system year."""
        current_year = datetime.now().year
        return current_year - self.birth_year

    def get_id(self) -> str:
        """Public method to safely access private ID."""
        return self._internal_id


# --------------------------------
# 2️⃣ Subclasses (Inheritance) - Specialization
# --------------------------------
class MuseumStaff(Person):
    def __init__(self, name: str, birth_year: int, id_number: str, role: str):
        # Initializing parent attributes
        super().__init__(name, birth_year, id_number)
        self.role = role

    def __str__(self):
        return f"Staff: {self.name} | Role: {self.role}"

class Artist(Person):
    def __init__(self, name: str, birth_year: int, id_number: str, style: str):
        super().__init__(name, birth_year, id_number)
        self.style = style

    def __str__(self):
        return f"Artist: {self.name} | Style: {self.style}"


# --------------------------------
# 3️⃣ Domain Class (Exhibit) - Composition (Exhibit HAS AN Artist)
# --------------------------------
class Exhibit:
    def __init__(self, title: str, artist: Artist):
        self.title = title
        self.artist = artist   

    def show_info(self):
        print(f"🖼️ Exhibit: {self.title}")
        print(f"👨‍🎨 Created by: {self.artist.name} ({self.artist.style})")
        print(f"📅 Artist Age: {self.artist.calculate_age()} years old")
        print("-" * 30)


# --------------------------------
# 4️⃣ Composition Class (Gallery) - Container logic
# --------------------------------
class Gallery:
    def __init__(self, name: str):
        self.name = name
        self._exhibits = []  # Private list to manage collection

    def add_exhibit(self, exhibit: Exhibit):
        self._exhibits.append(exhibit)
        print(f"✅ '{exhibit.title}' added to {self.name}")

    def list_exhibits(self):
        print(f"\n--- 🏛️ Welcome to {self.name} ---")
        if not self._exhibits:
            print("The gallery is currently empty.")
        for exhibit in self._exhibits:
            exhibit.show_info()


# --------------------------------
# 5️⃣ Main Program (Execution)
# --------------------------------
if __name__ == "__main__":
    # 1. Create Artist Objects (Inheriting from Person)
    da_vinci = Artist("Leonardo da Vinci", 1452, "ART001", "High Renaissance")
    picasso = Artist("Pablo Picasso", 1881, "ART002", "Cubism")

    # 2. Create Staff (Inheritance)
    staff1 = MuseumStaff("Adam", 2000, "STF-99", "Curator")

    # 3. Create Exhibit Objects (Composition)
    exhibit1 = Exhibit("Mona Lisa", da_vinci)
    exhibit2 = Exhibit("Guernica", picasso)

    # 4. Manage Gallery
    my_gallery = Gallery("Neustadt Modern Art Wing")
    my_gallery.add_exhibit(exhibit1)
    my_gallery.add_exhibit(exhibit2)

    # 5. Show Results
    my_gallery.list_exhibits()

    # 6. Test Encapsulation & Inheritance
    print(f"Verification: {staff1.name}'s ID is {staff1.get_id()}")
