# Function to check if a number is prime
def is_prime(num):
    # Ask the user to enter a number 
    num = int(input("Enter a number:"))
    # Variable to track if number is prime
    prime = True

    if num <= 1:
        prime = False
    else:
        # Loop from 2 up to sqrt(num)
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                prime = False
                break # Exit loop early if advisor is found


            # Conditional output
            if prime:
                print(num, "is a prime number.")
            else:
                print(num, "is NOT a prime number.")

        # Test (Debugging)
        is_prime(8)
        is_prime(3)
        is_prime(2)                   