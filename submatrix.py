import random

class Submatrix():

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.matrix = [[int(random.getrandbits(1)) for x in range(width)] for y in range(height)]
        self.output = [[0 for x in range(width)] for y in range(height)]

    def calculate(self):
        print "Randomly generated input"
        self.print_sub_matrix(self.matrix)

        #copy first coloum as is.
        for index, item in enumerate(self.matrix):
            self.output[index][0] = item[0]

        #copy first row as is
        self.output[0] = self.matrix[0]

        current_max = 0
        current_max_h = 0
        current_max_w = 0
        for h in range(1, self.height):
            for w in range(1, self.width):
                if self.matrix[h][w]:
                    self.output[h][w] = min(
                        1 + self.matrix[h - 1][w - 1],
                        1 + self.matrix[h][w - 1],
                        1 + self.matrix[h - 1][w]
                    )
                    if self.output[h][w] > current_max:
                        current_max = self.output[h][w]
                        current_max_h = h
                        current_max_w = w


                else:
                    self.output[h][w] = 0

        print "Output"
        self.print_sub_matrix(self.output)

        print "Max square matrix of size %s at %s,%s" % (current_max, current_max_h, current_max_w)

    def print_sub_matrix(self, m):
        for x in m:
            print x

m = Submatrix(5, 7)

m.calculate()

