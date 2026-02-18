import sys

from functools import reduce

# List of exhibit titles
exhibits = ["mona lisa", "starry night", "the thinker"]

# Using map with lambda to convert to uppercase
# lambda x: x.upper() is the transformation rule
result = map(lambda x: x.upper(), exhibits)

# Converting map object to a list to see the output
print(list(result))



# List of exhibition years
years = [1885, 1905, 1950, 1999, 2010, 1922]

# Goal: Keep only years from the 20th century (1900-1999)
# Condition: year >= 1900 and year <= 1999
filtered_years = filter(lambda y: 1900 <= y <= 1999, years)

# Convert to list and print
print(list(filtered_years))

# Task 3: Lambda function for 10% insurance tax
insurance_tax = lambda value: value * 0.1

# Example usage
price = 1000
tax = insurance_tax(price)

print(f"Original Price: {price}")
print(f"Calculated Tax (10%): {tax}")




# Task 4: Replicating map using List Comprehension
exhibit_titles = ["mona lisa", "starry night", "the thinker"]

# This does the same as map(lambda x: x.upper(), exhibit_titles)
# but in a more Pythonic way
uppercase_titles = [title.upper() for title in exhibit_titles]

print("Original Titles:", exhibit_titles)
print("Uppercase Titles (via Comprehension):", uppercase_titles)

# Task 5: A Pure Function
# This function only depends on its arguments (a, b)
# It produces no side effects (no print, no global changes)

def add_exhibits(current_count, new_additions):
    """
    Pure Function: Calculates total exhibits.
    Input -> Output only.
    """
    return current_count + new_additions

# Testing the Pure Function
total = add_exhibits(10, 5)
print(f"Total Exhibits: {total}")



# Original list
numbers = list(range(1000))

# 1. Functional Approach (Creates a new list)
new_numbers = [x * 2 for x in numbers]
print(f"Memory of new list: {sys.getsizeof(new_numbers)} bytes")

# 2. In-place modification (Traditional - modifies same memory)
# This is NOT functional programming, but it's memory efficient
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(f"Memory of original list: {sys.getsizeof(numbers)} bytes")


# Data collection
prices = [120, 450, 300, 80]

# Approach A: Functional Pattern using 'reduce'
# Processes the collection predictably without side effects
total_reduce = reduce(lambda x, y: x + y, prices)

# Approach B: Standard Accumulation Loop
total_loop = 0
for p in prices:
    total_loop += p

print(f"Reduce Total: {total_reduce} | Loop Total: {total_loop}")

# Raw Museum Data: (Name, Year, Value)
exhibits = [
    ("Mona Lisa", 1503, 800),
    ("The Scream", 1893, 120),
    ("Starry Night", 1889, 150),
    ("Guernica", 1937, 200)
]

# Building a Pipeline:
# 1. Filter: Keep only 19th-century items (1800-1899)
# 2. Map/Transform: Apply 10% insurance tax calculation
# 3. Final Result: List of tax values

pipeline_result = [
    item[2] * 0.1 
    for item in exhibits 
    if 1800 <= item[1] <= 1899
]

print(f"19th Century Insurance Taxes: {pipeline_result}")