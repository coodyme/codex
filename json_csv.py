import json
import csv
import os


def from_primary_key(json_path, csv_path):
    """
    Convert JSON Object with Primary Key to CSV

    Parameters:

    -json_path: Path to write JSON file
    -csv_path: Path to read CSV file

    JSON Example:
    {
        "primary_key":  { "key": "value" },
        "primary_key":  { "key": "value" }
    }
    """
    with open(json_path, mode='r') as json_file:
        items = json.load(json_file)

    for item in items:
        fields = list(items[item].keys())
        break

    with open(csv_path, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fields)

        writer.writeheader()

        for item in items:
            writer.writerow(items[item])


def from_dict(json_path, csv_path):
    """
    Convert JSON Object to CSV

    Parameters:

    -json_path: Path to write JSON file
    -csv_path: Path to read CSV file

    JSON Example:
    {
        "key": [
            { "key": "value" },
            { "key": "value" },
        ]
    }
    """
    with open(json_path) as json_file:
        json_data = json.load(json_file)

    data = json_data["id"]

    data_file = open(csv_path, mode='w')

    writer = csv.writer(data_file)

    count = 0

    for emp in data:
        if count == 0:

            header = emp.keys()
            writer.writerow(header)
            count += 1

        writer.writerow(emp.values())

    data_file.close()


def from_array(json_path, csv_path):
    """
    Convert JSON Array to CSV

    Parameters:

    -json_path: Path to write JSON file
    -csv_path: Path to read CSV file

    JSON Example:
    [
        { "key": "value" }
    ]
    """
    with open(json_path) as json_file:
        json_data = json.load(json_file)

    data_file = open(csv_path, mode='w', newline='')
    writer = csv.writer(data_file)

    count = 0
    for data in json_data:
        if count == 0:
            header = data.keys()
            writer.writerow(header)
            count += 1
        writer.writerow(data.values())

    data_file.close()


root = 'tmp'
export = 'export'

dirs = os.listdir(root)

for dir in dirs:
    files = os.listdir(f'./{root}/{dir}')
    files.sort()
    for file in files:
        print(f'Converting: {file} to CSV...')
        json_path = f"./{root}/{dir}/{file}"
        csv_path = f"./{export}/{dir}/{file.replace('.json', '')}.csv"
        from_array(json_path, csv_path)
        print('Done.')
