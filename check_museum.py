import json

# Reading the JSON file
with open('museum.json', 'r') as file:
    data = json.load(file)

# Printing the title
print('--- Museum Data Analysis ---')
print(f'Exhibit Title: {data["title"]}')
print(f'Creation Year: {data["year"]}')
