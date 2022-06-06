# truss-interview
CSV normalization submission for Alexander Do

Developed in Windows 10, tested in Docker ubuntu:latest container.

## Prerequisites:
- Install python on your device: sudo apt install python3


## How to run
1. Clone this repository to your desired directory.
2. CD to the aforementioned directory in your terminal.
3. Place your desired CSV file "input.csv" in the directory.
4. Run the command "python3 normalizer.py input.csv output.csv" in your terminal.

## Follow-ups:
- Writing tests for remaining functions
- Scaling for larger CSV files
- Handling edge cases that were not necessary to account for in the scope of this assignment
  - Missing data
  - ZIPs with more than 5 digits
  - Ill-formatted data values
