#!/usr/bin/python3
"""0. UTF-* Validation"""


def decimalToBinary(dps):
    return [bin(dp).replace("0b", "") for dp in dps]


def validUTF8(data):
    """a method that determines if a given data
    set represents a valid UTF-8 encoding.
    """
    if len(data) == 0:
        return False
    datapoints = decimalToBinary(data)
    i = 0
    while i < len(datapoints):
        bnum = datapoints[i]
        while len(bnum) < 8:
            bnum = '0' + bnum
        if bnum[0] == '1':
            j = 0
            count = 0
            while bnum[j] == '1':
                count += 1
                j += 1
            q = i + 1
            for w in range(count):
                if not datapoints[q].startswith('10'):
                    return False
                q += 1
            i = q
        else:
            i += 1
    return True
