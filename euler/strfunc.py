def longest_repetatinve_substring(str):
    matrix = [[0 for i in range(len(str))] for i in range(len(str))]
    for i, x in enumerate(str):
        for j, y in enumerate(str):
            if i == 0 or j == 0:
                matrix[i][j] = 1 if x == y else 0
            elif x == y:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = 0
    return matrix


def longest_repeated_substring_no_overlap(str):
    pass

def string_reverse(str):
    return str[::-1]


if __name__ == "__main__":
    print longest_repetatinve_substring("abcabc") #abcd
    print longest_repeated_substring_no_overlap("abcabcsdf")
    print string_reverse("Hello world")

