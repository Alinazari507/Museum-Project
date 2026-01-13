import json
import yaml

# 1. Load the JSON data
with open('museum.json', 'r') as json_file:
    data = json.load(json_file)

# 2. Save the data as a YAML file
with open('museum_converted.yaml', 'w') as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=False)

print('✅ Conversion Successful: museum.json -> museum_converted.yaml')
