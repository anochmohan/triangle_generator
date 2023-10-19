#!/usr/bin/env python3

import sys
pattern = sys.argv[1]
num_lines = sys.argv[2]

def triangle(shape: str, length: int) -> str|int:
    """Takes in a pattern and number of lines to return a triangle
    
    Args:
        shape: a string
        lines: a number
    """

    # To convert string length to int
    length = int(length)

    # For each column
    for i in range(0, (length//2)+1):
        # For each row
        for j in range(0, i):
            print(shape, end=" ")
        # Print the downward pattern
        print()
    
    # if statement  to check odd/even
    if (length % 2  == 0):
        # if even, then add one more column
        for i in range((length-1)//2, -1, -1):
            for j in range(0, i+1):
                print(pattern, end=" ")
            print()
    else:
        for i in range((length-1)//2, -1, -1):
            for j in range(0, i+1):
                print(pattern, end=" ")
            print()


triangle(pattern, num_lines)