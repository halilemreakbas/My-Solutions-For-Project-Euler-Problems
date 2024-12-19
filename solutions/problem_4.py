#The problem asks:
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
#9009 = 91 x 99
#Find the largest palindrome made from the product of two 3-digit numbers.



def is_palindrome(number):
    # convert number to string, reverse it and check it
    return str(number) == str(number)[::-1]


largest_palindrome = 0
for num1 in range(999, 99, -1):  # from 999 to 100 
    for num2 in range(num1, 99, -1):  # from num1 to 100
        product = num1 * num2  # take product of these numbers
        if is_palindrome(product):  # is that polindrom ?
            largest_palindrome = max(largest_palindrome, product)  # save the largest one


print(largest_palindrome)  # so the answer is "906609"


