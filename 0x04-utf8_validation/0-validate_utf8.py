#!/usr/bin/python3
""" 0-validate_utf8 """


def count_leading_ones(byte):
    """ Helper function to count the number of leading 1 bits in a byte """

    count = 0
    for i in range(8):
        if (byte >> (7 - i)) & 1:
            count += 1
        else:
            break
    return count


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding """
    data = iter(data)
    for leading_byte in data:
        leading_ones = count_leading_ones(leading_byte)
        if leading_ones == 1 or leading_ones > 4:
            return False
        if leading_ones == 0:
            continue
        for _ in range(leading_ones - 1):
            trailing_byte = next(data, None)
            if trailing_byte is None or \
                    trailing_byte >> 6 != 0b10:
                return False
    return True
