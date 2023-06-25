# factorial

import numpy as np

def factorial(num):
    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result

def f2(n):
    if n == 1:
        return 1
    return f2(n-1) * n

res = factorial(3)
print(res)
res2 = f2(3)
print(res2)

