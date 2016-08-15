def initialize_matrix(rows, coloum, fill=0):
    return [[fill for i in range(coloum)] for i in range(rows)]

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print matrix[i][j],
        print ""


if __name__ == "__main__":
    i = initialize_matrix(4,4,1)
    print_matrix(i)