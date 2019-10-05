import turtle
import random


def tree(branchLen, t, p=None):
    p = branchLen // 6
    r = random.randint(10, 20)
    l = random.randint(10, 20)
    angle = random.randint(15, 45)
    if branchLen < 35:
        t.color("green")

    if branchLen > 5:
        t.pensize(p)
        t.forward(branchLen)
        t.right(angle)
        tree(branchLen - r, t)
        # t.color("gray")
        t.left(20 + angle)
        tree(branchLen - l, t)
        t.right(angle)

        t.backward(branchLen)
        t.color("gray")


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color("gray")
    tree(100, t)
    myWin.exitonclick()


import turtle


def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, myTurtle):
    colormap = ["blue", "red", "green", "white", "yellow", "violet", "orange", "gray", "purple", "cyan", "black"]
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski(
            [points[0], getMid(points[0], points[1]), getMid(points[0], points[2])],
            degree - 1,
            myTurtle,
        )
        sierpinski(
            [points[1], getMid(points[0], points[1]), getMid(points[1], points[2])],
            degree - 1,
            myTurtle,
        )
        sierpinski(
            [points[2], getMid(points[2], points[1]), getMid(points[0], points[2])],
            degree - 1,
            myTurtle,
        )


def main_func():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-500, -250], [0, 500], [500, -250]]
    sierpinski(myPoints, 6, myTurtle)
    myWin.exitonclick()


main_func()
