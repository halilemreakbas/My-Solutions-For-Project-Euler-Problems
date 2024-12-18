# The problem asks: 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000. 
# Approaching to the Problem:
# Step 1: Loop through all numbers from 1 to 999.
# Step 2: For each number, check if it is divisible by 3 or 5 using the modulus operator (%).
# Step 3: If the number is divisible by either, add it to the total sum.

total = 0  # Total sum

# 1 to 999 range <1000
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0: 
        total += i  # add to total

print(total) # so the answer is  "233168"
