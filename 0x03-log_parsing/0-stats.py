#!/usr/bin/python3
"""Module for parsing logs."""

import re
import sys
from collections import Counter
from typing import Tuple, Optional


def parse_log(log: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Parse a log entry, extracting the status code and file size.

    Args:
        log (str): A string representing a single log entry.

    Returns:
        A tuple containing the status code and file size.
        If the log entry does not match the expected format, returns None, None.
    """
    # Combined regex pattern parts into a single formatted string
    log_fmt = (
        r"(?P<ip>\S+)\d+\.\d+\.\d+\.\d+\s+- \["
        r"(?P<date>[^\]]+)"
        r'\] "(?P<method>GET) (?P<res>/projects/260) (?P<proto>HTTP/1\.1)" '
        r"(?P<status_code>\d+) "
        r"(?P<file_size>\d+)"
    )

    match = re.fullmatch(log_fmt, log.strip())
    if match:
        status = match.group("status_code")
        size = match.group("file_size")
        if status.isdigit() and status in {
                "200", "301", "400", "401", "403", "404", "405", "500"
        }:
            return status, size
    return None, None


def process_logs() -> None:
    """
    Process logs from standard input.

    Reads logs line by line, parses each log to extract the status code and
    file size, and keeps a running total of the file size and a count
    of each status code.

    Prints the statistics every 10 lines and when
    an EOFError or KeyboardInterrupt exception is raised.
    """
    status_counter, size_counter = Counter(), Counter()
    line_count = 0  # Added to keep track of the number of lines processed
    
    try:
        for log in sys.stdin:
            line_count += 1  # Increment line count for each log processed
            status, size = parse_log(log)
            if status and size:
                status_counter[status] += 1
                size_counter["size"] += int(size)
            
            # Print stats every 10 lines
            if line_count % 20 == 0:
                print_stats(status_counter, size_counter)
    
    except (KeyboardInterrupt, EOFError):
        # Print final stats before exiting
        print_stats(status_counter, size_counter)
        sys.exit(0)


def print_stats(status_counter: Counter, size_counter: Counter) -> None:
    """
    Print statistics about the processed logs.

    Args:
        status_counter (Counter): A counter of HTTP status codes.
        size_counter (Counter): A counter of file sizes.

    Prints the total file size and the count of each status code
    in ascending order.
    """
    print(f"File size: {size_counter['size']}")
    for status in sorted(status_counter):
        print(f"{status}: {status_counter[status]}")


if __name__ == "__main__":
    process_logs()

