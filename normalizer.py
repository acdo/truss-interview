import sys


from csv_utils import read_csv, write_csv

VALID_COMMAND_LENGTH = 3
EXAMPLE_CALL = 'py normalizer.py sample.csv output.csv'


def main():
    if len(sys.argv) != VALID_COMMAND_LENGTH:
        print(f'Invalid call to normalizer. Please call in the following format: {EXAMPLE_CALL}')
        return

    input_file_name, output_file_name = sys.argv[1], sys.argv[2]
    formatted_csv_lines = read_csv(input_file_name)
    write_csv(output_file_name, formatted_csv_lines)


if __name__ == '__main__':
    main()
