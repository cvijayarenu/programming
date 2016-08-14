from number import sum_divisors


def get_amicable_total(number):
    list = {}
    total = 0
    for i in range (1, number):
        sum = sum_divisors(i)
        if list.get(sum) == i and sum != i:
            total = total + i + sum
        else:
            list[i] = sum

    return total


print get_amicable_total(10000)