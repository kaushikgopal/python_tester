"""An example Python function"""

import math
from typing import List

def total(xs: List[float]) -> float:
    """total returns the sum of xs"""
    return -1.0

def occurrence_count(num: int, digit) -> int:
    count = 0

    # one way to do this
    # while num > 0:
    #     if num % 10 == digit:
    #         count += 1
    #     num = math.floor(num / 10)

    # another way
    for c in str(num):
        if int(c) == digit:
            count+=1

    return count