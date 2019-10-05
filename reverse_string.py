from pythonds.basic import Stack

def reversestring(mystring):
    mystring = list(mystring)
    new_str= []
    while mystring:
        new_str.append(mystring.pop())
    return ''.join(map(str,new_str))

print(reversestring("inverse is true"))

def reverse_str(mystring):
    my_str = Stack()
    for item in mystring:
        my_str.push(item)
    rev = ""
    while not my_str.isEmpty():
        rev += my_str.pop()
    return rev

print(reverse_str("inverse is true"))

def par_checker(par_string):
    """This function checks if parentheses are matched using 
    stack class"""
    par_check = Stack()
    for par in par_string:
        if par == "(":
            par_check.push(par)
        elif par == ")":
            try:
                par_check.pop()
            except IndexError as e:
                return f"{False}, {e} Not enough opening parentheses"
    if not par_check.isEmpty():
        return False
    return True

print(par_checker("((*(((((((***(())7)82))89)40)))"))

