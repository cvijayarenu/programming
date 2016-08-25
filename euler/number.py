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

def is_prime(n):
    if n < 2 :
        return False
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def pimes_until(n):
    sieve = [True] * n
    for i in xrange(3, n, 2 ):
        if sieve[i]:
            for j in xrange(2*i, n, i):
                sieve[j] = False

def prime_series(start):
    while True:
        if is_prime(start):
            yield start
        start += 1

def is_pandigital_1to9(number):
    str_num = str(number)
    length = len(str_num)

    for i in range(1, length + 1):
        if str_num.find(str(i)) < 0:
            return False

    return True


if __name__ == "__main__":
    # print digit_sum(10)
    # print digit_sum(234)
    # print divisors(220)
    # print sum_divisors(220)
    # print is_prime(1)
    print is_pandigital_1to9(123456789)
    print is_pandigital_1to9(987654321)
    print is_pandigital_1to9(987654221)
    print is_pandigital_1to9(987655321)