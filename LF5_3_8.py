import sys
from functools import reduce

# --- Task 1: Mapping (Transformation) ---
# Transforming titles to uppercase using an anonymous lambda function.
exhibit_titles = ["mona lisa", "starry night", "the thinker"]
uppercase_map = list(map(lambda x: x.upper(), exhibit_titles))
print(f"Mapped Titles: {uppercase_map}")

# --- Task 2: Filtering ---
# Keeping only years belonging to the 20th century (1900-1999).
years = [1885, 1905, 1950, 1999, 2010, 1922]
century_20_years = list(filter(lambda y: 1900 <= y <= 1999, years))
print(f"Filtered Years (20th Century): {century_20_years}")

# --- Task 3: Lambda Functions ---
# Calculating a 10% insurance tax on exhibit values.
insurance_tax = lambda value: value * 0.1
price = 1000
print(f"Original Price: {price} | Calculated Tax: {insurance_tax(price)}")

# --- Task 4: Pure Functions & Immutability ---
# A pure function depends only on arguments and has no side effects.
def add_exhibits(current_count: int, new_additions: int) -> int:
    """Calculates total count without modifying external state."""
    return current_count + new_additions

total_items = add_exhibits(10, 5)
print(f"Pure Function Output (Total Exhibits): {total_items}")

# --- Task 5: Data Aggregation (Reduce) ---
# Using reduce to calculate the sum of all prices in the collection.
prices = [120, 450, 300, 80]
total_value = reduce(lambda x, y: x + y, prices)
print(f"Total Market Value: {total_value}")

# --- Task 6: Data Pipeline (Complex Transformation) ---
# Raw Museum Data format: (Title, Year, Value)
raw_exhibits = [
    ("Mona Lisa", 1503, 800),
    ("The Scream", 1893, 120),
    ("Starry Night", 1889, 150),
    ("Guernica", 1937, 200)
]

# Pipeline logic:
# 1. Filter: Keep 19th-century items (1800-1899).
# 2. Map/Transform: Calculate 10% tax.
pipeline_result = [
    item[2] * 0.1 
    for item in raw_exhibits 
    if 1800 <= item[1] <= 1899
]

print(f"Pipeline Result (19th Century Taxes): {pipeline_result}")