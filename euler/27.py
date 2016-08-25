def sum_of_spiral_diaognal(size):
    total = 0
    current_num = 1
    for i in range(1, size + 1):
        total = total + current_num
        current_num = current_num + 2 * i


    return total

print sum_of_spiral_diaognal(5)