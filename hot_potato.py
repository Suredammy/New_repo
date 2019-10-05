import random
import unittest
from collections import Counter

from pythonds.basic import Queue


def hot_potato(name, num=None):
    # num = random.randint(1,20)
    q = Queue()
    for n in name:
        q.enqueue(n)
    
    while q.size() > 1:
        for _ in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()


names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
freq = Counter([hot_potato(names, i) for i in list(range(55, 75))])
print(freq)


