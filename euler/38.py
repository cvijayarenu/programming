from number import is_pandigital_1to9
def p38():
    max = 0
    for i in range(1, 100000):
        product = get_product(i)
        if len(product[0]) != 9:
            continue

        if is_pandigital_1to9(product[0]):
            max = product[0]

    return max


def get_product(i):
    counter = 1
    total = ''
    while (len(str(total)) < 9):
        total += str(i * counter)
        counter += 1

    return total, counter


print p38()