#!/usr/bin/python3
"""Module for parsing logs."""

import re
import sys
import signal
from collections import defaultdict
from typing import Dict, Tuple, Optional


# Initialize metrics
file_size_total: int = 0
status_code_count: Dict[str, int] = defaultdict(int)


def parse_log(log: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Parse a log entry, extracting the status code and file size.

    Args:
        log (str): A string representing a single log entry.

    Returns:
        A tuple containing the status code and file size.
        If the log entry does not match the expected format,
        returns None, None.
    """
    parts = (
        r"(?P<ip>\S+)\d+\.\d+\.\d+\.\d+\s+",
        r"- \[",
        r"(?P<date>[^\]]+)",
        r'\] "(?P<method>GET) (?P<res>/projects/260) (?P<proto>HTTP/1\.1)" ',
        r"(?P<status_code>\d+)",
        r" ",
        r"(?P<file_size>\d+)",
    )

    log_fmt = "{}{}{}{}{}{}{}\\s*".format(
        parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6]
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


def print_stats() -> None:
    """
    Print statistics about the processed logs.
    """
    global file_size_total, status_code_count
    print(f"File size: {file_size_total}")
    for status in sorted(status_code_count):
        print(f"{status}: {status_code_count[status]}")


def handle_interrupt(signal_number: int, frame: Optional[None]) -> None:
    """
    Handles keyboard interrupt (CTRL+C) to print statistics and exit.

    Args:
        signal_number (int): The signal number.
        frame (Optional[None]): The current stack frame (not used).
    """
    print_stats()
    sys.exit(0)


def process_logs() -> None:
    """
    Process logs from standard input.

    Reads logs line by line, parses each log to extract the status code and
    file size, and keeps a running total of the file size and a count
    of each status code.

    Prints the statistics every 10 lines and when
    an EOFError or KeyboardInterrupt exception is raised.
    """
    global file_size_total, status_code_count
    line_count: int = 0

    # Register the signal handler for keyboard interruption
    signal.signal(signal.SIGINT, handle_interrupt)

    try:
        for line in sys.stdin:
            line_count += 1
            status, size = parse_log(line)
            if status and size:
                status_code_count[status] += 1
                file_size_total += int(size)

            # Print stats after every 10 lines
            if line_count % 10 == 0:
                print_stats()

    except (KeyboardInterrupt, EOFError):
        print_stats()
        sys.exit(0)
    except BrokenPipeError:
        # Handle the case where the pipe is broken (i.e.,
        # when the pipe is closed)
        sys.exit(0)


if __name__ == "__main__":
    process_logs()
