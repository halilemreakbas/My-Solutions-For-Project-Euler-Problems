#The problem asks:
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math
#lc = least common
def lc(x, y):
    # least common multiple of two numbers
    return abs(x * y) // math.gcd(x, y)

def smallest_multiple(n):
    result = 1
    for i in range(1, n + 1):
        result = lc(result, i)
    return result

# the smallest number divisible by all number from 1 to 20
n = 20
print(smallest_multiple(n))
