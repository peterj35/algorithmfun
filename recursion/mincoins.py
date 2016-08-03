def recMinCoins(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMinCoins(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

print(recMinCoins([1,5,10,25], 63))