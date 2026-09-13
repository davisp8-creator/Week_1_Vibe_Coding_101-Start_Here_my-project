#!/usr/bin/env python3
"""Print summary statistics for a CSV file."""

import argparse
import csv
import statistics
import sys


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def summarize(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        columns = {name: [] for name in fieldnames}
        row_count = 0
        for row in reader:
            row_count += 1
            for name in fieldnames:
                value = (row.get(name) or "").strip()
                if value != "":
                    columns[name].append(value)

    print(f"Rows: {row_count}")
    print(f"Columns: {len(fieldnames)}")
    print()

    for name in fieldnames:
        values = columns[name]
        missing = row_count - len(values)
        print(f"Column: {name}")
        print(f"  non-null: {len(values)}  missing: {missing}")

        if values and all(is_number(v) for v in values):
            numbers = [float(v) for v in values]
            print(f"  min: {min(numbers)}")
            print(f"  max: {max(numbers)}")
            print(f"  mean: {statistics.fmean(numbers):.4f}")
            print(f"  median: {statistics.median(numbers)}")
            if len(numbers) > 1:
                print(f"  stdev: {statistics.stdev(numbers):.4f}")
        else:
            unique = sorted(set(values))
            print(f"  unique values: {len(unique)}")
            preview = ", ".join(unique[:5])
            suffix = ", ..." if len(unique) > 5 else ""
            print(f"  sample: {preview}{suffix}")
        print()


def main():
    parser = argparse.ArgumentParser(description="Print summary statistics for a CSV file.")
    parser.add_argument("csv_path", help="Path to the CSV file")
    args = parser.parse_args()

    try:
        summarize(args.csv_path)
    except FileNotFoundError:
        print(f"Error: file not found: {args.csv_path}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
