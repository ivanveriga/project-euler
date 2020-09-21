# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


with open('task_3/first_10000_simple_nums.txt', 'r') as f:
    prime_factors = f.read().split()
    prime_factors = list(map(int, prime_factors))

num = 600851475143
multiplayers = []

def append_multiplayer(_num):
    for prime_factor in prime_factors:
        if _num % prime_factor == 0:
            multiplayers.append(prime_factor)
            return int(_num / prime_factor)

while num != 1:
    num = append_multiplayer(num)