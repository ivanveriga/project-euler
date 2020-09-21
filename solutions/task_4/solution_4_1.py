# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. 
# Find the largest palindrome made from the product of two 3-digit numbers.

palindromes = []

def pairs():
    for n_1 in range(999, 100, -1):
        for n_2 in range(999, 100, -1):
            yield n_1, n_2

def findPalindromes(_num_1, _num_2):
    mult_number = _num_1 * _num_2
    str_multnumber = str(mult_number)
    l = len(str_multnumber)
    str_mean = l//2
    str_multnumber_part_1 = str_multnumber[:str_mean]
    str_multnumber_part_2_reversed = str_multnumber[str_mean:][::-1]

    if str_multnumber_part_1 == str_multnumber_part_2_reversed:
        palindromes.append(mult_number)


for n_1, n_2 in pairs():
    findPalindromes(n_1, n_2)