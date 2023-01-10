#!/usr/bin/python3
"""
Minimum Operations module"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters in the file
    """
    # Solution 1: has some edge cases bugs
    # if n <= 1:
    #     return 0
    # i = 2
    # result = 0
    # while i <= n:
    #     if n % i == 0:
    #         result += i
    #         n /= i
    #     else:
    #         i += 1
    # return result

    # Solution 2: has some edge case bugs

    # if n <= 1:
    #     return 0

    # op = 'cp'
    # mem = 0
    # num_of_ops = 0
    # count_of_h = 0

    # while count_of_h + mem <= n:
    #     # print("op: {}, mem: {}, count_of_h: {}, num_of_ops: {}"
    #     #       .format(op, mem, count_of_h, num_of_ops))
    #     if op == 'cp':
    #         if mem is 0:
    #             mem = 1
    #         else:
    #             mem *= 2
    #         op = 'paste'
    #     else:
    #         count_of_h += mem
    #         op = 'cp'
    #     num_of_ops += 1
    # return num_of_ops

    # Solution 3: has some edge case bugs
    operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            operations += min_operations
            n /= min_operations
        min_operations += 1
    return operations
