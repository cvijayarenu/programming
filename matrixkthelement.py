from heapq import *


def getKmax(matrix, k):
    heap = []
    row = len(matrix)
    col = len(matrix[0])
    for i in range(col):
        heappush(heap, (matrix[0][i], 0, i))

    for j in range(k - 1):
        curr = heappop(heap)
        x = curr[1]
        y = curr[2]
        if x + 1 < row:
            heappush(heap, (matrix[x + 1][y], x + 1, y))

    return heap[0][0]


a = [[1, 5, 7, 10 , 11, 12], [3, 7, 8, 11, 13, 14], [4, 8, 9, 14, 15, 16]]

print getKmax(a, 4)