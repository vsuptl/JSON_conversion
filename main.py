import json
import csv

file_path = 'NCT03105011.json'

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

variables = data.get("protocolSection")

list_of_dicts = []

for key, value in variables.items():
    list_of_dicts.append(value)

rows = []
cols = []
for x in list_of_dicts:
    for key,value in x.items():
        if isinstance(value, str):#checks if the value is a string(Founded the row and col)
            rows.append(value)
            cols.append(key)
        elif isinstance(value, dict):#checks if the value is a dictionary(loop through the dict)
            for key,value in value.items():
                rows.append(value)
                cols.append(key)
        elif isinstance(value, list):#Checks if the value is a list(loop through list)
            cols.append(key)
            if isinstance(value[0], dict):#if the value is dict, loop through that
                for key,value in value[0].items():
                    rows.append(value)
            else:
                rows.append(value[0])#get the first value from list


filename = "conversion.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(cols)
    writer.writerow(rows)