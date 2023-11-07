#!/usr/bin/python3
import sys

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


# Define a function to print the statistics
def print_stats():
    global total_size, status_codes
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


# Loop through the lines of stdin
try:
    for line in sys.stdin:
        # Split the line by spaces
        tokens = line.split()
        # Check if the line has the expected format
        if len(tokens) > 2 and tokens[0].count(".")\
                == 3 and tokens[-1].isdigit():

            # Update the total file size
            total_size += int(tokens[-1])
            # Update the status code count
            if int(tokens[-2]) in status_codes:
                status_codes[int(tokens[-2])] += 1
        # Increment the line count
        line_count += 1
        # Print the statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    # Print the statistics after a keyboard interruption
    print_stats()
    raise
