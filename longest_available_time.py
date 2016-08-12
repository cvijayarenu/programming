
def find_max_free_time(input):
    list = []
    for x in input:
        list.append((x[0], 'S'))
        list.append((x[1], 'E'))
    list.sort()

    slots =  []
    slots.append(list[0][0] - 0) # 0 hours to starting.
    slots.append(24 - list[-1][0]) # last slot to end of day.

    # print list
    count = 0
    for i, v  in enumerate(list):
        if v[1] == 'S':
            count+= 1
        elif v[1] == 'E':
            count-= 1

        if count == 0 and i < len(list) - 1:
            slots.append(list[i+1][0] - list[i][0])

    return max(slots)

input = [(7, 10), (9, 11), (14, 19), (16, 17)]

print find_max_free_time(input)


