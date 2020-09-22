# A Pythagorean triplet is a set of three natural numbers, a < b < c, 
# for which, a^2 + b^2 = c^2 For example, 32 + 42 = 9 + 16 = 25 = 52. 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. 
# Find the product abc.

sum = 1000
a = 1

while a <= sum/3:
    b = a + 1

    while b <= sum/2:
        c = sum - a - b

        if a*a + b*b == c*c: pass

        b += 1

    a += 1