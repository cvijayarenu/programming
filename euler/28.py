# 1, 5, 9 17 25
# 4, 4, 8 8

def spiral_total(square_size):
    total = 0
    diognal = 1
    other_diognal = 1
    for i in range( square_size):
            diognal = diognal + (2*i)
            total += diognal
            if i % 2 == 1:
                other_diognal = other_diognal +  2 * i + 2
            else:
                other_diognal = other_diognal +  2 * i
            total += other_diognal

    return total -1

print spiral_total(1001)
