import pandas as pd
import json
#pip install openpyxl

# Load Excel to DataFrame
path_excel = 'data_book.xlsx'
df = pd.read_excel(path_excel, engine='openpyxl')

# Convert DataFrame to JSON
json_data = df.to_json(orient='records', indent=4)
print(json_data)

# Write JSON data to a file
path_json = 'data_json.json'
with open(path_json, 'w') as json_file:
    json_file.write(json_data)

if __name__ == '__main__':
    pass
