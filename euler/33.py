
def p33():
    den = 1
    num = 1
    for i in range(11,99):
        for j in range(i+1,99):
            if i % 10 == 0 and j % 10 == 0:
                # trivial options.
                continue
            k, l = reduce(i, j)

            if i == k and j == l:
                # can't reduce
                continue

            if i * l == j * k:

                num = num * i
                den = den * j

    return num, den


def reduce(i, j):
    if str(i)[0] in str(j)[0]:
        return int(str(i)[1]), int(str(j)[1])
    elif str(i)[0] in str(j)[1]:
        return int(str(i)[1]), int(str(j)[0])
    elif str(i)[1] in str(j)[0]:
        return int(str(i)[0]), int(str(j)[1])
    elif str(i)[1] in str(j)[1]:
        return int(str(i)[0]), int(str(j)[0])
    else:
        return i, j
print p33()