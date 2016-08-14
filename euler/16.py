def power_digit_sum_of_2(num):
    digits = 2 ** num
    total = 0
    while digits > 9:
        total += (digits % 10)
        digits /= 10
    total += digits
    return total


print power_digit_sum_of_2(1000)

print sum(int(x) for x in str(2**1000))