from number import is_prime, prime_series
def p37(number_of_primes):
    total = 0
    start_prime = 8
    count = 0
    for i in prime_series(start_prime):
        if is_trancatable_prime(i):
            # print i
            total += i
            count += 1
            if count == number_of_primes:
                break

    return total

def is_trancatable_prime(i):
    number = str(i)
    for i in range(1, len(number)):
        if not is_prime(int(number[i:])):
            return False


    for i in range(1, len(number)):
        if not is_prime(int(number[:len(number)-i])):
            return False

    return True

print p37(11)