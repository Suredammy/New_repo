import timeit


from functools import reduce
def product (x):
    return reduce(lambda a, b: a*b, x)

def product_1(y):
    ans = 1
    for i in y:
        ans *= i
    return ans


x = list(range(2000000))
popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop()", "from __main__ import x")
protime = timeit.Timer("product(list(range(1,20)))", "from __main__ import product")
protime_1= timeit.Timer("product_1(list(range(1,20)))", "from __main__ import product_1")
protime_2 = timeit.repeat("product_1(list(range(1,20)))", "from __main__ import product_1", repeat = 5, number = 100000)

print(min(protime_2))
print(protime_1)

print(popzero.timeit(1000))
print(popend.timeit(1000))
print(protime.timeit(100000))
print(protime_1.timeit(100000))
"""command line implementation"""
# python -m timeit -s"import timing" "timing.product(list(range(1,9)))"