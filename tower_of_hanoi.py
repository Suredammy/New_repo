import time
def moveTower(height, start, middle, end):
    if height >= 1:
        moveTower(height - 1, start, end, middle)
        showMove(start, end)
        moveTower(height - 1, middle, start, end)


def showMove(fr, to):
    print("Moving disk from {} to {}".format(fr, to))


# moveTower(4, "first", "middle", "last")
def pascal(n):

    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n - 1)
        for i in range(len(previous_line) - 1):
            line.append(previous_line[i] + previous_line[i + 1])
        line += [1]
    return line


# for i in range(1,500):
#         print(pascal(i))


def fib_pascal(n, fib_pos):
    if n == 1:
        line = [1]
        fib_sum = 1 if fib_pos == 0 else 0
    else:
        line = [1]
        (previous_line, fib_sum) = fib_pascal(n - 1, fib_pos + 1)
        for i in range(len(previous_line) - 1):
            line.append(previous_line[i] + previous_line[i + 1])
        line += [1]
        if fib_pos < len(line):
            fib_sum += line[fib_pos]
    return (line, fib_sum)


print(fib_pascal(6, 0))


def pascal_2(n):
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    line = [1]
    result = pascal_2(n - 1)
    last_row = (pascal_2(n - 1))[-1]
    for i in range(len(last_row) - 1):
        line.append(last_row[i] + last_row[i + 1])
    line += [1]
    result.append(line)
    return result


import pprint

pprint.pprint(pascal_2(5))

from turtle import *


time_1 = time.process_time()
class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        # self.pu()
        self.shapesize(1.2, n * 0.6, 3)  # square-->rectangle
        self.fillcolor(n/20, 1-n/20, .3)
        self.st()


class Tower(list):
    "Hanoi tower, a subclass of built-in type list"

    def __init__(self, x):
        "create an empty to20wer. x is x-position of peg"
        self.x = x

    def push(self, d):
        d.setx(self.x)
        d.sety(-250 + 30 * len(self))
        self.append(d)

    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d


def hanoi(n, from_, with_, to_):

    if n > 0:
        hanoi(n - 1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n - 1, with_, from_, to_)


def play(x):
    onkey(None, "space")
    clear()
    hanoi(x, t1, t2, t3)
    write("press STOP button to exit", align="center", font=("Courier", 16, "bold"))


def main(x):
    global t1, t2, t3
    ht()
    penup()
    goto(0, -225)  # writer turtle
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    # make tower of 6 discs
    for i in range(x, 0, -1):
        t1.push(Disc(i))
    # prepare spartanic user interface ;-)
    write("press spacebar to start game", align="center", font=("Courier", 16, "bold"))
    onkey(play(x), "space")
    listen()
    return "EVENTLOOP"


if __name__ == "__main__":
    num = int(input("Type the number of towers: "))
    msg = main(num)
    print(msg)
    mainloop()
    
 
time_2 = time.process_time()
print("Time takem is", time_2 -time_1)