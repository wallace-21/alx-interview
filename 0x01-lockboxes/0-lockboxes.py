#!/usr/bin/python3

"""import deque"""

from collections import deque

"""
    Declare a function called
"""


def canUnlockAll(boxes):
    """
        Function that determines if all the
        boxes can be opened

        Par:
            boxes (List[List[int]]): A list where each element is a list of
            integers representing the keys contained in that box.

    """
    n = len(boxes)
    # Set to track unlocked boxes
    unlocked = set()
    # Start with box 0
    queue = deque([0])

    while queue:
        box = queue.popleft()
        if box in unlocked:
            continue
        unlocked.add(box)
        for key in boxes[box]:
            if key < n and key not in unlocked:
                queue.append(key)

    return len(unlocked) == n
