#in effecient solution.
def recMC(coinValueList, change, knownResults):
    print coinValueList, change, knownResults
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return knownResults[change]
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numberCoins = 1 + recMC(coinValueList, change - i, knownResults)
            if numberCoins < minCoins:
                minCoins = numberCoins
                knownResults[change] = minCoins

    return minCoins

print recMC([1, 20, 100], 19, [0]*20)

