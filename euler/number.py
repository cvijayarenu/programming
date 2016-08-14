import math
def digit_sum(number):
    return sum(int(i) for i in str(number))

def factorial_recursive(number):
    lookup = {1:1}
    f = factorial(number, lookup)
    return f


def factorial(number, lookup):
    if lookup.get(number):
        return lookup.get(number)

    f = number * factorial(number - 1, lookup)
    lookup[number] = f
    return f


def factorial_iterative(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def divisors(num):
    if num == 1:
        return [1]
    return [i for i in range(1, num/2 + 1) if num % i == 0]


def no_of_divisors(num):
    if num == 1:
        return 1
    return sum(2 for i in range(1, int(math.sqrt(num)) + 1) if num % i == 0)


def sum_divisors(num):
    return sum(divisors(num))


if __name__ == "__main__":
    # print digit_sum(10)
    # print digit_sum(234)
    print divisors(220)
    print sum_divisors(220)