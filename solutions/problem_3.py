#The problem asks:
#The prime factors of 13195 are 5,7,13 and 29
#What is the largest prime factor of the number 600851475143 ?

#lpf = largest prime factor of a number
def lpf(n):
    factor = 2  # start with the smallest prime factor
    while factor * factor <= n:  # keep going while primefactor^2 doesn't exceed the number
        if n % factor == 0:  # if n is divisible by the current factor
            n //= factor  # divide n by the factor
        else:
            factor += 1  # move to the next factor
    return n  # the remaining value of n is the largest prime factor

# asked number
number = 600851475143
print(lpf(number))  #so the answer is "6857"
