import csv

from formatting_utils import *

def read_csv(file_name: str) -> list[dict[str]]:
    with open(file_name, encoding='utf-8', errors='ignore') as csvfile:
        csvreader = csv.DictReader(csvfile)
        return [format_line(line) for line in csvreader if format_line(line)]


def format_line(line: dict[str]) -> dict[str]:
    try:
        formatted_timestamp =


def write_csv():
    return