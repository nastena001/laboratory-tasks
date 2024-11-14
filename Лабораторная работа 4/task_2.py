import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []

        for row in reader:
            data.append(row)

    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME, encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
