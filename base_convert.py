from pythonds.basic import Stack
def base_covert(num, base):
    digits = "0123456789ABCDEF"
    converted_num = Stack()
    number = num
    while number > 0:
        number, rem = divmod(number, base)
        converted_num.push(rem)
    new_num = ""
    while not converted_num.isEmpty():
        new_num += digits[converted_num.pop()]
    
    return new_num
a = (base_covert(256, 16))
print(a)

from pythonds.basic import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["**"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("5 * 3 ** ( 4 - 2 )"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

    


    