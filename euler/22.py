import csv
def get_total_score(filename):
    names = []
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            for name in row:
                names.append(name)


    names.sort()

    total_score = 0
    for pos, name in enumerate(names):
        weight = get_weight(name)
        score = (pos + 1) * weight
        total_score += score

    return total_score


def get_weight(name):
    return sum(ord(c)-64 for c in name)

print get_total_score("p022_names.txt")

