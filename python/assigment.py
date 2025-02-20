# Find all numbers between 0 and 1000 which are prime numbers
# function is_prime will check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#  A better way to get all the prime numbers from 1 to n which cuts the number of iterations by half cause we are not checking the even numbers and checks only the odd numbers
def is_prime_better(num: int) -> bool:
    if num < 2 :
        return False
    for i in range(2, num):
        if num % (i ** 0.5) == 0:
            return False
    return True

def print_prime(n):
    for i in range(n):
        if is_prime(i):
            print(i)
        if is_prime_better(i):
            print(i)

# insert all the prime numbers into a list trough a nested for loop
prime_numbers = [i for i in range(1000) if is_prime_better(i)]

