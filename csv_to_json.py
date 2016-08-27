import csv
import json

csv_file = open('pokemon_info.csv', 'r')
json_file = open('pokemon_info.json', 'w')

fieldnames = ("Number", "Pokemon", "Type1", "Type2")
reader = csv.DictReader(csv_file, fieldnames)

for row in reader:
    json.dump(row, json_file)
    json_file.write('\n')