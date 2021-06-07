import os
from os import listdir
import csv_json
import json_csv
import shutil

ROOT = None
TEMP = 'temp'
EXPORT = 'export'
DIRS = []


def log():
    print('')


def dir_path(path):
    if os.path.isdir(path):
        return True
    else:
        print(
            f"{path} is not a valid path")
        return False


def setup_path():
    print()

    msg = 'Path to your root folder: '

    global ROOT
    ROOT = str(input(msg))

    while dir_path(ROOT) is not True:
        ROOT = str(input(msg))

    global DIRS
    DIRS = listdir(ROOT)

    for dir in DIRS:
        src = ROOT + '/' + dir
        dst = TEMP + '/' + dir
        shutil.copy(src, dst)

    print()


def show_examples():
    print('Primary Key')
    print()
    print("""
    {
      "primary_key":  { "key": "value" },
      "primary_key":  { "key": "value" }
    }
    """)
    print()

    print('Dict')
    print()
    print("""
    {
      "key": [
        { "key": "value" },
        { "key": "value" },
      ]
    }
    """)
    print()

    print('Array')
    print()
    print("""
    [
      { "key": "value" }
    ]
    """)
    print()


def show_menu():
    print()
    print('Choose an option: ')
    print()
    print('0 - Exit')
    print('1 - Show Examples')
    print()
    print('----------------------------------')
    print('CSV -> JSON')
    print('----------------------------------')
    print('2 - CSV to JSON (To Primary Key)')
    print('3 - CSV to JSON (To Dict)')
    print('4 - CSV to JSON (To Array)')
    print('----------------------------------')
    print('JSON -> CSV')
    print('----------------------------------')
    print('5 - JSON to CSV (From Primary Key)')
    print('6 - JSON to CSV (From Dict)')
    print('7 - JSON to CSV (From Array)')
    print()


def options():
    setup_path()
    show_menu()

    while True:
        opt = str(input('Option: '))
        if opt == '0':
            exit()
        elif opt == '1':
            show_examples()
        elif opt == '2':
            print('')
        elif opt == '3':
            print('')
        elif opt == '4':
            print('')
        elif opt == '5':
            print('5')
        elif opt == '6':
            print('6')
        elif opt == '7':
            print('7')
        else:
            print('Invalid Option')


def main():
    options()


if __name__ == '__main__':
    main()
