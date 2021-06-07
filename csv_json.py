import csv
import json


def to_primary_key(csv_path, json_path, primary_key):
    """
    Convert CSV to JSON mapped with a Primary Key

    Parameters:

    -csv_path: Path to read CSV file
    -json_path: Path to write JSON file
    -primary_key: Primary key to be the index of each item in JSON
    """
    data = {}

    with open(csv_path, encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file)

        for rows in reader:
            key = rows[primary_key]
            data[key] = rows

    with open(json_path, 'w', encoding='utf8') as json_file:
        json_file.write(json.dumps(data, indent=2, ensure_ascii=False))


def to_dict(csv_path, json_path, key):
    """
    Convert CSV to JSON

    Parameters:

    -csv_path: Path to read CSV file
    -json_path: Path to write JSON file
    -key: Dictionary key
    """
    data = {}
    data[key] = []

    with open(csv_path, mode='r', encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            data[key].append(row)

    with open(json_path, mode='w', encoding='utf8') as json_file:
        json_file.write(json.dumps(data, indent=2, ensure_ascii=False))


def to_array(csv_path, json_path):
    """
    Convert CSV to JSON

    Parameters:

    -csv_path: Path to read CSV file
    -json_path: Path to write JSON file
    """
    data = []

    with open(csv_path, encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file)

        for rows in reader:
            data.append(rows)

    with open(json_path, mode='w', encoding='utf8') as json_file:
        json_file.write(json.dumps(data, indent=2, ensure_ascii=False))


to_array('./temp/dez.csv', './temp/dez.json')
