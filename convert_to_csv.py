import json
import csv

with open('ctg-studies(3).json', 'r') as json_file:
    data = json.load(json_file)


def flatten_json(data):

    # Flatten a nested JSON structure to a flat dictionary.
    flattened = {}

    def flatten(item, name=''):
        if type(item) is dict:
            for key in item:
                flatten(item[key], name + key + '_')
        elif type(item) is list:
            i = 0
            for value in item:
                flatten(value, name + str(i) + '_')
                i += 1
        else:
            flattened[name[:-1]] = item

    flatten(data)
    return flattened

def convert_json_to_csv(json_data, csv_file):
   
    # Convert JSON data to CSV and save it to a file.
  
    flattened_data = flatten_json(json_data)
    # print(flattened_data)
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=flattened_data.keys())
        writer.writeheader()
        writer.writerow(flattened_data)

csv_file = 'output.csv'
convert_json_to_csv(data, csv_file)
print(f"JSON data successfully converted and saved to {csv_file}")



