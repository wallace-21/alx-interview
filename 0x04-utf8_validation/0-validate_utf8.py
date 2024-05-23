#!/usr/bin/env python3

"""Define a methood validUTF"""


def validUTF8(data):
    """acceepts a list of integers"""
    for nums in data:
        if nums > 255:
            return False

    return True
