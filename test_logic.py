#!/usr/bin/env python3
import json

# Load the data
with open('primal_animals.json', 'r') as f:
    primal_data = json.load(f)

def is_date_in_range(month, day, start, end):
    """Check if date falls within the range"""
    date_value = month * 100 + day
    start_value = start['month'] * 100 + start['day']
    end_value = end['month'] * 100 + end['day']

    if start_value <= end_value:
        # Normal range (doesn't cross year boundary)
        return date_value >= start_value and date_value <= end_value
    else:
        # Range crosses year boundary (e.g., Dec 22 - Jan 19)
        return date_value >= start_value or date_value <= end_value

def find_sign(year, month, day):
    """Find the primal sign for a given date"""
    year_str = str(year)
    if year_str not in primal_data:
        return None

    year_data = primal_data[year_str]
    for sign in year_data:
        if is_date_in_range(month, day, sign['start'], sign['end']):
            return sign
    return None

# Test cases
test_dates = [
    (2025, 1, 1, "Eagle"),      # Start of year
    (2025, 1, 20, "Leopard"),   # Mid-January
    (2025, 2, 20, "Frog"),      # February
    (2025, 6, 22, "Snail"),     # June
    (2025, 12, 31, "Alligator"), # End of year
]

print("Testing primal sign lookup logic:")
print("-" * 60)

for year, month, day, expected in test_dates:
    result = find_sign(year, month, day)
    if result:
        status = "✓" if result['sign'] == expected else "✗"
        print(f"{status} {year}/{month:02d}/{day:02d}: {result['sign']:20} (expected: {expected})")
    else:
        print(f"✗ {year}/{month:02d}/{day:02d}: No match found (expected: {expected})")

print("\nAll tests completed!")
