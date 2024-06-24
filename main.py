import json
import csv

file_path = 'ctg-studies.json'

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

first_section = data[0].get("protocolSection")

print(first_section)