class Person:
    def __init__(self, name, birth_year, id_number):
        self.name = name
        self.birth_year = birth_year
        self._internal_id = id_number

    def calculate_age(self, current_year):
        age = current_year - self.birth_year
        return age

class MuseumStaff(Person):
    def __init__(self, name, birth_year, role, id_number):
        super().__init__(name, birth_year, id_number)
        self.role = role
staff1 = MuseumStaff("Ali", 1985, "Manager", "MB208")
staff2 = MuseumStaff("Zahra", 2000, "Guide", "MB214")

print(staff1.name)
print(staff1.role)
print(staff1.birth_year)
print(staff1.calculate_age(2026))

print(staff2.name)
print(staff2.role)
print(staff2.birth_year)
print(staff2.calculate_age(2026))



class Artist(Person):
    def __init__(self, name, birth_year, id_number, style):
        super().__init__(name, birth_year, id_number)
        self.style = style




da_vinci = Artist("Da vinci", 1452, "AR2006", "High Renaissance")
picasso = Artist("picasso", 1881, "ART5008", "Surrealism")
print(da_vinci.name)
print(da_vinci.birth_year)
print(da_vinci.calculate_age(2026))
print(da_vinci.style)

print(picasso.name)
print(picasso.birth_year)
print(picasso.calculate_age(2026))
print(picasso.style)








