
def get_longest_recurring_cycle(max):
    curr_max = (0,0)
    for i in range(2, max):
        frac = get_franction(i)
        if frac > curr_max[0]:
            curr_max = (i, frac)
    return curr_max[0]


def get_franction(num):
    fraction = []
    divisor = 10
    while divisor not in fraction:
        fraction.append(divisor)
        divisor = (divisor % num) * 10
        if divisor in fraction or divisor == 0:
            break

    return len(fraction)

print get_longest_recurring_cycle(1000)

