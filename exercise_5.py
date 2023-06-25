import numpy as np

def square_sum(num):
    if num == 1:
        return 1
    return num * num + square_sum(num-1)

print(square_sum(4))


# 20230626 add

def b():
    return True