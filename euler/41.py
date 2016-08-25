from number import is_prime, rwh_primes, is_pandigital_1to9
def p41(limit):
    primes = rwh_primes(limit)
    for i in reversed(primes):
        if is_pandigital_1to9(i):
            return i

#print p41(10)
print p41(7654321)