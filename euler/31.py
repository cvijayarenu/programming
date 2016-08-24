def get_max_possible_changes(coin_list, amount):

    no_of_possibilites = [1] + [0]* amount

    for coin in coin_list:
        for x in range(coin, amount+1):
            no_of_possibilites[x] += no_of_possibilites[x - coin]

    return no_of_possibilites[amount]

print get_max_possible_changes([1, 2, 5, 10, 20, 50, 100, 200], 200)