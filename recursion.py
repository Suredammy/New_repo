def sum(array):
    if len(array) == 1:
        return array[0]
    return array[0] + sum(array[1:])


mylist = list(range(21))
print(sum(mylist))
mylist = mylist


def convert_base(number, base):
    convertString = "0123456789ABCDEF"
    if number < base:
        return convertString[number]
    else:
        num, rem = divmod(number, base)
        return convert_base(num, base) + convertString[rem]


print(convert_base(10, 2))
print(convert_base(32, 16))

def leave_alpha(string):
    return "".join(i for i in string.lower() if i.isalpha())

def reverse_word(mystring):
    def check_pal(string):
        if len(string) == 1:
            return string
        else:
            return check_pal(string[1:]) + string[0]
    if check_pal(mystring) == mystring:
        return True
    else: return False
    
string = leave_alpha("Reviled did I live, said I, as evil I did deliver")
print(reverse_word(string))


import turtle
myTurtle = turtle.Turtle()
myprint = turtle.Screen()

def spiral(myTurtle, length):
    if length > 0:
        myTurtle.forward(length)
        myTurtle.right(45)
        #myTurtle.forward(length)
        #myTurtle.right(90)
        spiral(myTurtle, length -1)

spiral(myTurtle, 50)
myprint.exitonclick()


    

