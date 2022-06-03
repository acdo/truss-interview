import csv
import sys

from formatting_utils import *

FIELD_NAMES = ['Timestamp', 'Address', 'ZIP', 'FullName', 'FooDuration', 'BarDuration', 'TotalDuration', 'Notes']


def read_csv(file_name: str) -> list[dict[str]]:
    with open(file_name, encoding='utf-8', errors='ignore') as csvfile:
        csvreader = csv.DictReader(csvfile)
        return [format_line(line) for line in csvreader if format_line(line)]


def format_line(line: dict[str]) -> dict[str]:
    try:
        formatted_timestamp = format_timestamp(line['Timestamp'])
        formatted_address = format_address(line['Address'])
        formatted_zip = format_zip(line['ZIP'])
        formatted_name = line['FullName'].upper()
        formatted_foo_duration = format_duration(line['FooDuration'])
        formatted_bar_duration = format_duration(line['BarDuration'])
        formatted_total_duration = str(float(formatted_foo_duration) + float(formatted_bar_duration))
        formatted_notes = line['Notes']      # Already preformatted when passed through csvreader

        return {
            'Timestamp': formatted_timestamp,
            'Address': formatted_address,
            'ZIP': formatted_zip,
            'FullName': formatted_name,
            'FooDuration': formatted_foo_duration,
            'BarDuration': formatted_bar_duration,
            'TotalDuration': formatted_total_duration,
            'Notes': formatted_notes
        }

    except ValueError:
        sys.stderr.write(f'Invalid value found in line {line}, removing from formatted csv.\n')
        return {}


def write_csv(file_name: str, lines: list[dict[str]]) -> None:
    with open(file_name, 'w', encoding='utf-8', errors='ignore', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
        writer.writeheader()
        for line in lines:
            writer.writerow(line)

