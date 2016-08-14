from number import *


def factorial_sum(number):
    f = factorial_iterative(number)
    return digit_sum(f)

print factorial_sum(100)