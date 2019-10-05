import math
def gcd(a, b):
    if b == 0:
        return a
    else: return gcd(b, a%b)

def gcd2(a, b):

    while b:
        a, b = b, a%b
    return a


def volume(c1, c2, vol):
    """ The water is poured from the from_cup to the to_cup
    until the desired volume, vol, is reached"""
    from_cup, to_cup = c1, 0
    
    if vol%math.gcd(c1, c2) != 0 or vol > max(c1, c2): #check if it is possible to solve 
        return "The puzzle cannot be solved"
    count = 1  #The initial count needed to fill the jug above
    array = [(from_cup, to_cup)]
    while from_cup != vol and to_cup != vol:
        #find the maximum amount that can be poured
        temp = min(from_cup, c2 - to_cup)

        #pour "temp" from from_cup to to_cup
        to_cup += temp
        from_cup -= temp
        count += 1
        array.append((from_cup, to_cup))
        if from_cup == vol or  to_cup == vol:
            break
        #if first cup becomes empty, fill it
        if from_cup == 0:
            from_cup = c1
            count += 1
            array.append((from_cup, to_cup))

        #if second cup becomes full, empth it
        if to_cup == c2:
            to_cup = 0
            count += 1
            array.append((from_cup, to_cup))   

    return count, array, vol
print(volume(18,11,11))
print(volume(11,18,13))


import sys
import logging
logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(levelname)s -%(message)s")
#logging.disable(level = logging.debug)
        

        

