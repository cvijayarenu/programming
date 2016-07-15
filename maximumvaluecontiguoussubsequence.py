
class MaxValContiguous():

    def __init__(self, input):
        self.input = input

    def findMaxVal(self):
        self.length = len(self.input)
        self.output = []
        self.output.insert(0, self.input[0])

        for index in xrange(1, self.length):
            max_till_now = max(
                self.output[index - 1] + self.input[index],
                self.input[index]
            )
            self.output.insert(index, max_till_now)
        print self.output

input = [2, -3, 4]
x = MaxValContiguous(input=input)
x.findMaxVal()