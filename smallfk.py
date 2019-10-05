class Interpreter:
    """ The rules for the interpreter are below
    > - Move pointer to the right (by 1 cell)
    < - Move pointer to the left (by 1 cell)
    * - Flip the bit at the current cell
    [ - Jump past matching ] if value at current cell is 0
    ] - Jump back to matching [ (if value at current cell is nonzero)"""

    def __init__(self):
        pass
        

    def __call__(self, code, tape):
        tape = list(tape)
        code_pointer = 0
        cell = 0
        while (-1 < cell < len(tape)) and (code_pointer < len(code)):
            if code[code_pointer] == ">":
                cell += 1
            elif code[code_pointer] == "<":
                cell -= 1
            elif code[code_pointer] == "*":
                if tape[cell] == "0":
                    tape[cell] = "1"
                elif tape[cell] == "1":
                    tape[cell] = "0"

            elif code[code_pointer] == "[":
                if tape[cell] == "0":
                    step = 1
                    while step != 0:
                        code_pointer += 1
                        if code[code_pointer] == "[":
                            step += 1
                        elif code[code_pointer] == "]":
                            step -= 1

            elif code[code_pointer] == "]":
                if tape[cell] != "0":
                    back = 1
                    while back != 0:
                        code_pointer -= 1
                        if code[code_pointer] == "]":
                            back += 1
                        elif code[code_pointer] == "[":
                            back -= 1
                code_pointer -= 1
                    

            code_pointer += 1

        return "".join(map(str, tape))


class PaintFk:
    def __init__(self, code, iterations, width, height):
        self.row = width
        self.col = height
        self.t = iterations
        self.code = code

    def drawGrid(self):
        data_grid = [[0 for r in range(self.row)] for c in range(self.col)]
        return data_grid

    def read_code(self):
        stack, bracket_pos = [], {}
        for i, c in enumerate(self.code):
            if c == "[": 
                stack.append(i)
            elif c == "]": 
                bracket_pos[i] = stack[-1]
                bracket_pos[stack.pop()] = i

        grid = self.drawGrid()
        a, b = 0, 0
        p = 0
        while self.t > 0 and p < len(self.code):
            if self.code[p] == "e": b += 1
            elif self.code[p] == "w": b -= 1
            elif self.code[p] == "s": a += 1
            elif self.code[p] == "n": a += 1
            elif self.code[p] == "*": grid[a][b] ^= 1
            elif (self.code[p] == "[" and grid[a][b] == 0) or\
            (self.code[p] == "]" and grid[a][b] == 1): 
                p = bracket_pos[p]
            self.t -= 1
            p += 1
        final = "\r\n".join("".join(map(str, g)) for g in grid)
        return final
        


pa = PaintFk("ee*e*e*ss[this is just a comment]*w*esswn*n*e*", 23, 5, 7)
print(pa.read_code(), end = "")



