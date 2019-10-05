def coin_num(coinValue, change, cache):
    mincoins = change
    if change in coinValue:
        cache[change] = 1
        return 1

    elif cache[change] > 0:
        return cache[change]

    else:
        for i in [c for c in coinValue if c <= change]:
            numcoins = 1 + coin_num(coinValue, change - i, cache)
            if numcoins < mincoins:
                mincoins = numcoins
                cache[change] = mincoins
    return mincoins


def dp_coin(coins_value, change, mincoins=None, coins_used=None):
    mincoins = [0] * (change + 1)
    coins_used = [0 for i in range(change + 1)]
    for cents in range(change + 1):
        coin_count = cents
        coin_list = [c for c in coins_value if c <= cents]
        for j in coin_list:
            if mincoins[cents - j] + 1 < coin_count:
                coin_count = mincoins[cents - j] + 1
              
        mincoins[cents] = coin_count
        
    return mincoins[change]
    


print(dp_coin([1, 5, 8, 10, 25], 33))

