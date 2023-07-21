#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
status code> <file size> (if the format is not this one,
the line must be skipped)"""


import sys


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

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
        if status_code in status_codes:
            status_codes[status_code] += 1

        # Print metrics every 10 lines or keyboard interruption
        if (i + 1) % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_codes):
                print(f"{code}: {status_codes[code]}")
            print()

except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
