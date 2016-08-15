def find_index_lenth_1000(length):
    fib = {}
    fib[0] = 0
    fib[1] = 1
    for i in range(2, 100000):
        fib[i] = fib[i-1] + fib[i-2]
        if len(str(fib[i])) > length - 1:
            print i, fib[i]
            break
    return i


print find_index_lenth_1000(1000)