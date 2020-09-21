# The sum of the squares of the first ten natural numbers is,
# The square of the sum of the first ten natural numbers is,
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

numbers = range(1, 101)
sum_squares = sum([n**2 for n in numbers])
square_sum = sum(numbers) ** 2
diff = square_sum - sum_squares