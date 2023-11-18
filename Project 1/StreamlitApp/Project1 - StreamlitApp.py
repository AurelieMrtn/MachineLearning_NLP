# Import combined_sores
import json

file_path = 'combined_scores.json'

with open(file_path, 'r') as file:
    loaded_dict = json.load(file)

print(f"The dictionary has been loaded from {file_path}: {loaded_dict}")
