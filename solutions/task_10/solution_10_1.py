# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math


def isPrime(x):

    if x % 2 == 0 and x != 2:
        return False

    for i in range(3, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
        
    return True


print(sum([i if isPrime(i) else 0 for i in range(2, 2_000_000)]))