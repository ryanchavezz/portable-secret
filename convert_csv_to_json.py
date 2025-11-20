#!/usr/bin/env python3

import csv
import json
from datetime import datetime

# Month mapping
MONTHS = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
    'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
    'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

def parse_date(date_str):
    """Parse 'Jan 01' format to {month, day}"""
    parts = date_str.split()
    if len(parts) != 2:
        raise ValueError(f"Invalid date format: '{date_str}'")
    month_name = parts[0]
    if month_name not in MONTHS:
        raise ValueError(f"Invalid month: '{month_name}' in date '{date_str}'")
    day = int(parts[1])
    return {'month': MONTHS[month_name], 'day': day}

def create_link(sign):
    """Create primal-astrology.com link from sign name"""
    # Convert to lowercase and replace spaces with hyphens
    slug = sign.lower().replace(' ', '-')
    return f"https://www.primal-astrology.com/primalzodiac/{slug}"

# Read CSV and organize by year
data_by_year = {}

with open('primal_animals.csv', 'r') as f:
    reader = csv.DictReader(f)
    row_num = 0
    for row in reader:
        row_num += 1
        try:
            year = row['Year']

            # Skip header rows that appear in the data
            if year == 'Year':
                continue

            sign = row['Primal Sign']

            entry = {
                'sign': sign,
                'start': parse_date(row['Start Date']),
                'end': parse_date(row['End Date']),
                'link': create_link(sign)
            }

            if year not in data_by_year:
                data_by_year[year] = []

            data_by_year[year].append(entry)
        except Exception as e:
            print(f"Error on row {row_num}: {e}")
            print(f"Row data: {row}")
            raise

# Write to JSON file
with open('primal_animals.json', 'w') as f:
    json.dump(data_by_year, f, indent=2)

print(f"Successfully converted CSV to JSON!")
print(f"Total years: {len(data_by_year)}")
print(f"Output file: primal_animals.json")
