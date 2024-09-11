#!/usr/bin/python3
"""Read from stdin and parse the logs"""
import sys


files_size = 0
status = {}
line_count = 0


def update_stats(file_size: str, lstatus: str):
    """Update the statistics"""
    global files_size
    try:
        file_size = int(file_size)
        files_size += file_size
    except ValueError:
        pass
    try:
        lstatus = int(lstatus)
        status[lstatus] = status.get(lstatus, 0) + 1
    except ValueError:
        pass


def print_status(status: dict):
    """Print count of status"""
    sorted_keys = sorted(status.keys())
    for key in sorted_keys:
        print("{}: {}".format(key, status.get(key)))


try:
    for line in sys.stdin:
        line_count += 1
        splitted_line = line.strip().split()
        if len(splitted_line) == 9:
            update_stats(splitted_line[-1], splitted_line[-2])
        if line_count == 10:
            print("File size: {}".format(files_size))
            print_status(status)
            line_count = 0
    if line_count % 10 != 0:
        print("File size: {}".format(files_size))
        print_status(status)
except KeyboardInterrupt:
    print("File size: {}".format(files_size))
    print_status(status)
    raise
