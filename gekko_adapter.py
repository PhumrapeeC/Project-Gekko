import csv
import json

class GekkoAdapter():
    def __init__(self):
        pass

    def json_to_csv(json_data, csv_filename):
        with open(csv_filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            
            writer.writerow(json_data[0].keys())
            
            for item in json_data:
                writer.writerow(item.values())