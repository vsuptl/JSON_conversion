import json
import csv

file_path = 'ctg-studies.json'

with open(file_path, 'r') as file:
    data = json.load(file)