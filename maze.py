import turtle

PART_OF_PATH = "O"
Tried = "."
Obstacle = "+"
DEAD_END = "-"


class Maze:
    def __init__(self, mazeFilename):
        rowsinMaze = 0
        columnsinMaze = 0
        self.mazelist = []
        with open(mazeFilename, "r") as f:
            for line in f:
                rowlist, col = [], 0
                for ch in line[:-1]:
                    rowlist.append(ch)
                    if ch == "S":
                        self.startRow = rowsinMaze
                        self.startCol = col
                    col += 1
                rowsinMaze += 1
                self.mazelist.append(rowlist)
                columnsinMaze = len(rowlist)

        self.rowsinMaze = rowsinMaze
        self.columnsinMaze = columnsinMaze
        self.xTranslate = -columnsinMaze / 2
        self.yTranslate = rowsinMaze / 2
        self.t = turtle.Turtle()
        self.t.shape = turtle.Turtle(shape="square")
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(
            -(columnsinMaze - 1) / 2 - 0.5,
            -(rowsinMaze - 1) / 2 - 0.5,
            (columnsinMaze - 1) / 2 + 0.5,
            (rowsinMaze - 1) / 2 + 0.5,
        )

    def drawMaze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rowsinMaze):
            for x in range(self.columnsinMaze):
                if self.mazelist[y][x] == Obstacle:
                    self.drawCenteredBox(
                        x + self.xTranslate, -y + self.yTranslate, "green"
                    )
        self.t.color("gray")
        self.t.fillcolor("blue")
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self, x, y, color):
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moveTurtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.xTranslate, -y + self.yTranslate))
        self.t.goto(x + self.xTranslate, -y + self.yTranslate)

    def dropBreadcrumb(self, color):
        """To show the squares we have visited"""
        self.t.dot(10, color)

    def updatePosition(self, row, col, val=None):
        if val:
            self.mazelist[row][col] = val
        self.moveTurtle(col, row)
        if val == PART_OF_PATH:
            color = "green"
        elif val == Obstacle:
            color = "red"
        elif val == Tried:
            color = "black"
        elif val == DEAD_END:
            color = "red"
        else:
            color = None
        if color:
            self.dropBreadcrumb(color)

    def isExit(self, row, col):
        return (
            row == 0
            or row == self.rowsinMaze - 1
            or col == 0
            or col == self.columnsinMaze - 1
        )

    def __getitem__(self, idx):
        return self.mazelist[idx]


def searchFrom(maze, startRow, startColumn):
    maze.updatePosition(startRow, startColumn)
    # Check for base cases:
    # 1. We have run into an obstacle, return False
    if maze[startRow][startColumn] == Obstacle:
        return False
    # 2. A square has already been explored.
    if maze[startRow][startColumn] == Tried:
        return False
    # 3. Successfully exit, an outside edge is not occupied by an obstacle
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, Tried)
    # Else, try each direction in turn
    found = (
        searchFrom(maze, startRow - 1, startColumn)
        or searchFrom(maze, startRow + 1, startColumn)
        or searchFrom(maze, startRow, startColumn - 1)
        or searchFrom(maze, startRow, startColumn + 1)
    )
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found


myMaze = Maze("maze2.txt")
myMaze.drawMaze()
myMaze.updatePosition(myMaze.startRow, myMaze.startCol)
searchFrom(myMaze, myMaze.startRow, myMaze.startCol)
