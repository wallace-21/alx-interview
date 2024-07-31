#!/usr/bin/python3
"""Module for parsing logs."""
import re
import sys
from collections import Counter
from typing import Tuple, Optional


def parse_log(log: str) -> Tuple[Optional[str], Optional[int]]:
    """
    Parse a log entry, extracting the status code and file size.
    Args:
        log (str): A string representing a single log entry.
    Returns:
        A tuple containing the status code and file size.
        If the log entry does not match the expected format,
        returns None, None.
    """
    # Regex pattern to match the log format
    log_fmt = (
        r"(?P<ip>\S+) - - \[(?P<date>[^\]]+)\] "
        r'"(?P<method>GET) (?P<res>/projects/260) (?P<proto>HTTP/1\.1)" '
        r"(?P<status_code>\d+) (?P<file_size>\d+)"
    )

    match = re.match(log_fmt, log.strip())
    if match:
        status = match.group("status_code")
        size = int(match.group("file_size"))
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
    status_counter, size_counter = Counter(), 0
    line_count = 0

    try:
        for log in sys.stdin:
            line_count += 1
            status, size = parse_log(log)
            if status and size is not None:
                status_counter[status] += 1
                size_counter += size

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(status_counter, size_counter)

    except (KeyboardInterrupt, EOFError):
        pass

    finally:
        # Print final stats before exiting
        print_stats(status_counter, size_counter)
        sys.exit(0)


def print_stats(status_counter: Counter, size_counter: int) -> None:
    """
    Print statistics about the processed logs.
    Args:
        status_counter (Counter): A counter of HTTP status codes.
        size_counter (int): A counter of the total file size.
    Prints the total file size and the count of each status code
    in ascending order.
    """
    print(f"File size: {size_counter}")
    for status in sorted(status_counter.keys()):
        print(f"{status}: {status_counter[status]}")


if __name__ == "__main__":
    process_logs()
