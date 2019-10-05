import sys
import logging
logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(levelname)s -%(message)s")
def knapsack(v, w, W, n = None):
    """n number of items, where i items has a value, v[i] and 
    weight, w[i] for a total weight of W"""
    n = max(len(v), len(w))
    v, w = [0] + v, [0] + w
    
    #create a table of n+1 rows and W+1 columns
    t = [[0 for col in range(W+1)] for row in range(n+1)]

    for j in range(W+1):
        t[0][j] = 0

    for i in range(1, n+1):
        for j in range(W+1):
            if w[i] > j:
                t[i][j] = t[i-1][j]

            else:
                t[i][j] = max(t[i-1][j], t[i-1][j -w[i]] + v[i])

    return t[n][W]

weight = [240, 135, 2800, 410, 182]
calorie =  [900, 650, 5000, 950, 95]


volume = [40, 400, 1500, 410, 190]
# print("True","18200")
# print(knapsack(volume * 120, calorie * 120, 5500))


def knap(val, wt, W, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W]
w = [2, 3, 4, 5, 9]
v = [3, 4, 8, 8, 10]
val = [60, 100, 120]
wei = [10, 20, 30]

#jprint(knapsack(calorie, weight, 9500))
#print(knapsack(calorie, volume, 5500))
# print(knapsack(val, wei, 50))
# print()
# print(knap(v, w, 20, 5))

memo = {}
def Maxload(values, w):
    if w in memo:
        return memo[w]
    if w <= 0:
        return 0
    if not values:
        return 0
    max = 0
    for v in values:
        if v > w:
            continue
        res = Maxload(values, w-v) + v
        if res > max:
            max = res
    
    memo[w] = max
    # logging.debug(memo)
    return memo[w]



