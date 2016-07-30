
class MaxValContiguous():

    def __init__(self, input):
        self.input = input

    def findMaxVal(self):
        self.length = len(self.input)
        final_max = self.output = [self.input[0]]
        for index in xrange(1, self.length):
            max_till_now = max(
                self.output[index - 1] + self.input[index],
                self.input[index]
            )
            self.output.insert(index, max_till_now)
            final_max = max(max_till_now, final_max)
        print self.output
        print final_max

input = [1, -3, 2, 2]
x = MaxValContiguous(input=input)
x.findMaxVal()