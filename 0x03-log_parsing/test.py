#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime
from collections import defaultdict

def print_metrics(file_sizes, status_codes):
    total_size = sum(file_sizes)
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def process_lines(lines):
    file_sizes = []
    status_codes = defaultdict(int)

    for line in lines:
        try:
            ip, _, _, _, _, status_code, file_size = line.split()[0], line.split()[6], line.split()[8], line.split()[9], line.split()[10], line.split()[11]
            file_size = int(file_size)
            status_code = int(status_code)

            file_sizes.append(file_size)
            status_codes[status_code] += 1

        except (ValueError, IndexError):
            continue

        if len(file_sizes) % 10 == 0:
            print_metrics(file_sizes, status_codes)
            print()

try:
    lines = []
    for i in range(10000):
        sleep(random.random())
        line = "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
            random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
            datetime.datetime.now(),
            random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
            random.randint(1, 1024)
        )
        sys.stdout.write(line)
        sys.stdout.flush()
        lines.append(line)

        if len(lines) % 10 == 0:
            process_lines(lines)
            lines = []

except KeyboardInterrupt:
    process_lines(lines)
