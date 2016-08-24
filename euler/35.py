from itertools import permutations
from number import is_prime

def p35(limit):
    circular_primes = []
    prime_set  = set([1, 2])
    for i in range(3, limit+1):
        print i
        if is_prime(i):
            prime_set.add(i)

    print sorted(prime_set)

    for i in range(11939, limit+1):
        for s in permutations(str(i), len(str(i))):
            if int(''.join(s)) not in prime_set:
                #found a non prime set
                break
        else:
            print i
            circular_primes.append(i)

    return len(circular_primes)

print p35(1000000)