import csv
import json

def csv_to_json(csv_file_path, json_file_path):
  #Read csv and add to dic
  data = []
  with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file) #this wouldmake it a dictionary
    for row in csv_reader:
      data.append(row)

  #write data in json file
  with open(json_file_path, mode="w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4)


csv_to_json("./csv_to_json/csvData.csv", "newjson")
