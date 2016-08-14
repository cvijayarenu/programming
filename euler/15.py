def recPath(rows, coloum):
    result = [[0 for x in range(coloum + 1)] for y in range(rows + 1)]
    for r in range( rows + 1):
        for c in range( coloum + 1):
            if r == 0 or r == 0:
                result[r][c] = 1
            else:
                result[r][c] = result[r-1][c] + result[r][c-1]

    return result[rows][coloum]

if __name__ == "__main__":
    print recPath(20, 20)