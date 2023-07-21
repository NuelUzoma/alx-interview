#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
status code> <file size> (if the format is not this one,
the line must be skipped)"""


import sys


total_size = 0
status_codes = {}

try:
    # Read input line by line
    for i, line in enumerate(sys.stdin):
        # Parse input format
        try:
            parts = line.split()
            file_size = int(parts[8])
            status_code = int(parts[10])
        except Exception as e:
            # Skip if input format isnt the right one
            continue

        # Update metrics
        total_size += file_size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1

        # Print metrics every 10 lines or keyboard interruption
        if (i + 1) % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_codes):
                print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")
