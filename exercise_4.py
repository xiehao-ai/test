import numpy as np


def isPrime(number):
    if number <= 1:
        print(f'\n illegal input: {number}! The input should be greater than 1 \n')
        return False
    else:
        for i in range(2, number//2 + 1):
            if number % i == 0:
                return False
        return True


def print_Prime(start, end):
    for i in range(start, end + 1):
        if isPrime(i):
            print(i)


print_Prime(1, 25)













