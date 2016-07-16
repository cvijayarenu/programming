# in efficient solution. recursive model
def recMC(coinValueList, change, knownResults):
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

# iterative model
def dpMakeChange(coinValueList,change,minCoins):
   for cents in range(change+1):
      coinCount = cents
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
      minCoins[cents] = coinCount
   return minCoins[change]

print dpMakeChange([1, 5, 10], 11, [0]*12)
