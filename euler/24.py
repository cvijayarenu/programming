from itertools import *

def nth_lexiogaphic_permutation(inputvalues, pos):

    return ''.join(list(permutations(inputvalues, len(inputvalues)))[pos])

print nth_lexiogaphic_permutation("0123456789",999999)

