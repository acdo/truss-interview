import sys


from csv_utils import read_csv, write_csv

VALID_COMMAND_LENGTH = 3
EXAMPLE_CALL = 'python3 normalizer.py input.csv output.csv'


def main():
    """
    Takes in input csv path from input, formats its lines, and outputs to specified path.

    :return: None
    """

    if len(sys.argv) != VALID_COMMAND_LENGTH:
        print(f'Invalid call to normalizer. Please call in the following format: {EXAMPLE_CALL}')
        return
    input_file_name, output_file_name = sys.argv[1], sys.argv[2]

    try:
        formatted_csv_lines = read_csv(input_file_name)
    except OSError:
        sys.stderr.write(f'Specified input file {input_file_name} not found, exiting.\n')
        return

    try:
        write_csv(output_file_name, formatted_csv_lines)
    except OSError:
        sys.stderr.write(f'Output file could not be written, please try again.\n')


if __name__ == '__main__':
    main()
