#!/usr/bin/env python3

'''
OPS445 Assignment 2 - Winter 2023
Program: assignment2.py
Author: Walid Hasan Ansary

The python code in this file is original work written by
Walid Hasan Ansary. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or online resource. I have not shared this Python script
with anyone or anything except for submission for grading.

I understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Description:
This program displays Linux system memory usage using a bar graph.
Milestone 1 includes functions for converting a percentage to a graph
and reading total and available memory from /proc/meminfo.

Date: July 14, 2026
'''

import argparse
import os
import sys


def parse_command_args() -> object:
    """Set up command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Memory Visualiser -- See Memory Usage Report with bar charts"
        ),
        epilog="Copyright 2023"
    )

    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=20,
        help="Specify the length of the graph. Default is 20."
    )

    parser.add_argument(
        "program",
        type=str,
        nargs="?",
        help=(
            "if a program is specified, show memory use of all associated "
            "processes. Show only total use if not."
        )
    )

    args = parser.parse_args()
    return args


def percent_to_graph(percent: float, length: int = 20) -> str:
    """Turn a percentage from 0.0 to 1.0 into a bar graph."""
    filled_length = round(percent * length)
    empty_length = length - filled_length

    return "#" * filled_length + " " * empty_length


def get_sys_mem() -> int:
    """Return the total system memory in kB."""
    with open("/proc/meminfo", "r") as meminfo:
        for line in meminfo:
            if line.startswith("MemTotal:"):
                return int(line.split()[1])

    return 0


def get_avail_mem() -> int:
    """Return the currently available system memory in kB."""
    with open("/proc/meminfo", "r") as meminfo:
        for line in meminfo:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1])

    return 0


def pids_of_prog(app_name: str) -> list:
    """Given an application name, return all associated process IDs."""
    pass


def rss_mem_of_pid(proc_id: str) -> int:
    """Given a process ID, return the resident memory used."""
    pass


def bytes_to_human_r(kibibytes: int, decimal_places: int = 2) -> str:
    """Convert kibibytes into a human-readable memory value."""
    suffixes = ["KiB", "MiB", "GiB", "TiB", "PiB"]
    suffix_count = 0
    result = kibibytes

    while result > 1024 and suffix_count < len(suffixes) - 1:
        result /= 1024
        suffix_count += 1

    string_result = f"{result:.{decimal_places}f} "
    string_result += suffixes[suffix_count]

    return string_result


if __name__ == "__main__":
    args = parse_command_args()

    if not args.program:
        pass
    else:
        pass
