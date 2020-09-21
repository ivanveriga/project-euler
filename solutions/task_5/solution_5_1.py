# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import itertools
from math import prod

PRIME_FACTORS = [2, 3, 5, 7, 11, 13, 17, 19]

def get_next_factor(num):
    for f in PRIME_FACTORS:
        if num % f == 0:
            return f

least_common_multiple = 1

for num in range(2, 21):
    big_num = least_common_multiple if least_common_multiple > num else num
    small_num = least_common_multiple if least_common_multiple < num else num

    big_num_factors = []
    small_num_factors = []

    while big_num > 1:
        next_factor = get_next_factor(big_num)
        big_num_factors.append(next_factor)
        big_num /= next_factor

    while small_num > 1:
        next_factor = get_next_factor(small_num)
        small_num_factors.append(next_factor)
        small_num /= next_factor

    multiplayers = big_num_factors.copy()

    for snf in small_num_factors:
        if snf in big_num_factors:
            del big_num_factors[big_num_factors.index(snf)]
        else:
            multiplayers.append(snf)

    least_common_multiple = prod(multiplayers)