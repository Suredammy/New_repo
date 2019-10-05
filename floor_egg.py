import sys
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def eggfloor(egg, floor):
    # We need 0 trail for 0 floor and only 1 trial for 1 floor
    if floor == 0 or floor == 1:
        return floor

    # We need k trials for one egg and k floors
    if egg == 1:
        return floor

    min = sys.maxsize
    for x in range(1, floor + 1):
        res = 1 + max(eggfloor(egg - 1, floor - 1), eggfloor(egg, floor - x))
        if res < min:
            min = res

    return min


# print(eggfloor(2, 10))


# A Dynamic Programming based Python Program for the Egg Dropping Puzzle
INT_MAX = 32767

# Function to get minimum number of trials needed in worst
# case with e eggs and f floors
def eggDrop(egg, floor):
    # A 2D table where entery eggFloor[e][f] will represent minimum
    # number of trials needed for e eggs and f floors.
    eggfloor = [[0 for e in range(floor + 1)] for f in range(egg + 1)]

    # We need one trial for one floor and 0 trials for 0 floors
    for e in range(1, egg + 1):
        eggfloor[e][1] = 1
        eggfloor[e][0] = 0

    # We always need f trials for one egg and f floors.
    for f in range(1, floor + 1):
        eggfloor[1][f] = f

    # Fill rest of the entries in table using optimal substructure
    # property
    for e in range(2, egg + 1):
        for f in range(2, floor + 1):
            eggfloor[e][f] = sys.maxsize
            for x in range(1, floor + 1):
                res = 1 + max(eggfloor[e - 1][x - 1], eggfloor[e][f - x])
                if res < eggfloor[e][f]:
                    eggfloor[e][f] = res

    return eggfloor[egg][floor]
    # eggFloor[egg][floor] holds the result


def binomial(n, k):
    if 0 <= k <= n:
        nCk, kCk = 1, 1
        for i in range(1, min(k, n - k) + 1):
            nCk *= n
            kCk *= i
            n -= 1
        return nCk // kCk
    else:
        return 0


from functools import lru_cache


from timer import total, bestoftotal
import sympy


def height(egg, trial):

    if egg == 0 or trial == 0:
        return 0
    if egg > trial:
        return trial
    sum = 0
    cache = [0] * (trial + 1)
    cache[0] = 1
    for i in range(1, trial + 1):
        cache[i] = 1
        j = i - 1
        while j > 0:
            cache[j] += cache[j - 1]
            j -= 1

    for i in range(1, egg + 1):
        sum += cache[i]

    return sum

def heigh(n, m):  
    ret=0
    trm=1       #every term
    for i in range(n):
        trm = trm*(m-i)//(i+1)
        ret+=trm
    return ret

def heig(egg, trial):
    becof = 1
    sum = 0
    for i in range(1,egg+ 1):
        becof = becof * (trial - i +1) // i
        sum += becof
    return sum

# print(bestoftotal(10,100,heig, 190,200))


# print(bestoftotal(10, 100, heigh, 19000, 20000))



MOD = 998244353
haha_inv = [0, 1]
for haha_i in range(2, 80000 + 1):
    haha_inv.append((MOD - MOD // haha_i) * haha_inv[MOD % haha_i] % MOD)


# def height(n, m):
#     h, t = 0, 1
#     m %= MOD

#     for i in range(1, n + 1):
#         t = t * (m - i + 1) * haha_inv[i] % MOD
#         h = (h + t) % MOD
#     return h % MOD
