# Prime Number Checker

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Assume number is prime
isPrime = True

# Check conditions
if num <= 1:
    isPrime = False
else:
    for i in range(2, num // 2 + 1):  # loop from 2 up to num/2
        if num % i == 0:  # if divisible
            isPrime = False
            break  # stop checking further

# Final output
if isPrime:
    print(num, "is a Prime number.")
else:
    print(num, "is NOT a Prime number.")
