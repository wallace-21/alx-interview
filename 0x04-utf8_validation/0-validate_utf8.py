#!/usr/bin/python3

"""Define a methood validUTF"""


def validUTF8(data):
    """acceepts a list of integers"""
    bytes_of_num = 0
    for nums in data:
        if nums > 255:
            return False

        if bytes_of_num == 0:
            """check how many bytes the current number indicates"""
            if (nums >> 5) == 0b110:
                bytes_of_num = 1
            elif (nums >> 4) == 0b1110:
                bytes_of_num = 2
            elif (nums >> 3) == 0b11110:
                bytes_of_num = 3
            elif (nums >> 7):
                return False
        else:
            """Check that the next bytes are continuation bytes"""
            if (nums >> 6) != 0b10:
                return False
            bytes_of_num -= 1

    return True
