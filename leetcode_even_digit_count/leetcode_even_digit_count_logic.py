"""
Given an array nums of integers
return how many of them contain an even number of digits
in [12, 345, 2, 7896]

12 contains 2 digits (even)
345 contains 3 digits (odd)
2 contains 1 digit (odd)
7896 contains 4 digits (even)
"""
import math
from typing import List

def event_digit_count(arr: List[int]) -> int:
    # return len([n for n in arr if len(str(n)) % 2 == 0])
    filtered = [n for n in arr if (int(math.log10(n)) + 1) % 2 == 0]
    return len(filtered)