# Step 1: Define the generic Parent Class
class Person:
    def __init__(self, name, birth_year, id_number):
        self.name = name
        self.birth_year = birth_year
        # Private attribute
        self._internal_id = id_number

# Step 2: Create a Subclass that inherits from Person
class MuseumStaff(Person):
    def __init__(self, name, birth_year, id_number, role):
        # Inherit: Use super() to call the Parent's constructor
        super().__init__(name, birth_year, id_number)
        # Add a specific attribute for this subclass
        self.role = role

# Step 3: Instantiate a MuseumStaff object
staff_member = MuseumStaff("Adam", 2000, "STAFF-99", "Guide")

# Testing the inheritance
print(f"Staff Name: {staff_member.name}") # Inherited from Person
print(f"Staff Role: {staff_member.role}") # Specific to MuseumStaff
print(f"Staff Birth Year: {staff_member.birth_year}") # Inherited from Person