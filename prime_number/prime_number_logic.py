
from cmath import sqrt
import math


def is_prime(num) -> bool:
    n = 2
    while n*n <= num:
        if num % n == 0:
            return False
        n = n + 1

    return True

    # upper_bound = math.isqrt(num) + 1
    #  for x in range(2, upper_bound):
    #      if num % x == 0:
    #          return False
    # return True