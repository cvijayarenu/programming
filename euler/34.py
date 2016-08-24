def p34():
    lookup= {
        0:1,
        1:1,
        2:2,
        3:6,
        4:24,
        5:120,
        6:720,
        7:5040,
        8:40320,
        9:362880
    }
    final_total = 0
    for number in range(3, 5000000):
        total = 0
        for digit in str(number):
            total += lookup.get(int(digit))
        if total == number:
            final_total += number
            print number

    return final_total

print p34()
