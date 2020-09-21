# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def isPrime(num):
    factors = []

    for n in range(1, num):
        if num % n == 0:
            factors.append(n)

        if len(factors) > 2:
            return False 

    return True if len(factors) < 2 else False


count = 10001
last_num = 1

while count >= 0:
    if isPrime(last_num):
        count -= 1

    last_num += 1


# NON EFFECTIVE METHOD but it work