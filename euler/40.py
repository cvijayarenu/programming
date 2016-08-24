def p40(n):
    count = 1
    product  = 1
    for i in get_fraction(1):
        if count == 1 or count == 10 or count == 100 or count == 1000 or count == 10000 or count == 100000 or count == 1000000:
            product *= i

        count += 1
        if count > n :
            break

    return product


def get_fraction(number):
    str_num = str(number)
    while True:
        yield int(str_num[0])
        str_num = str_num[1:]
        if not str_num:
            number += 1
            str_num = str(number)
print p40(1000001)