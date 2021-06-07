import os
import csv
import sys

TMP = 'tmp'
EXPORT = 'export'

dirs = os.listdir(TMP)

for dir in dirs:
    files = os.listdir(f"./{TMP}/{dir}")

    files.sort()

    rows = []

    fieldnames = None

    for file in files:
        file_path = f"{TMP}/{dir}/{file}"
        print()
        print(f"Opening: {file}")
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            fieldnames = csv_reader.fieldnames
            print(f"Appending rows...")
            for i, row in enumerate(csv_reader):
                sys.stdout.write(
                    "\r" + f"Append: {i}")
                rows.append(row)
                sys.stdout.flush()

    print()
    print(f"Writing {dir}.csv")
    with open(f"./{EXPORT}/{dir}.csv", mode="w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames)

        writer.writeheader()

        for row in rows:
            writer.writerow(row)
    print('Process end.')
