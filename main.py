
import csv
from database import load_data


def extract_data():

    with open("data/sensor_data.csv", "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    print("Data extracted successfully!")
    print("Total records:", len(data))

    return data


def transform_data(data):

    clean_data = []
    seen = set()

    for row in data:

        key = tuple(row.values())

        if key in seen:
            continue

        seen.add(key)

        if not row["temperature"] or not row["humidity"]:
            continue

        row["temperature"] = float(row["temperature"])
        row["humidity"] = float(row["humidity"])

        clean_data.append(row)

    print("\nTransformation completed!")
    print("Clean records:", len(clean_data))

    return clean_data


if __name__ == "__main__":

    raw_data = extract_data()

    clean_data = transform_data(raw_data)

    load_data(clean_data)
