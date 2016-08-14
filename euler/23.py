from number import sum_divisors
from itertools import *
from sets import Set

#
# def sum_of_positive_two_abadant_numbers():
#     set = Set(range(1, 28124))
#     an = get_abundant_number(28123)
#     com = combinations_with_replacement(an, 2)
#     setb = Set([sum(i) for i in com])
#     setc = set & setb
#     return sum(setc)
#
#
# def get_abundant_number(limit):
#     result = []
#     for i in range(12, limit+1):
#         s = sum_divisors(i)
#         if s > i:
#             result.append(i)
#     return result
#
# print sum_of_positive_two_abadant_numbers()


abundants = set(i for i in range(1,28124) if sum_divisors(i) > i)

def abundantsum(i):
    return any(i-a in abundants for a in abundants)

print sum(i for i in range(1,28124) if not abundantsum(i))





