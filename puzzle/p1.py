"""
Leetcode:  Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5

"""
operators = ['+', '-', '*', '/']


def calculate(s):

    tokens = toRPN(s)
    return evalRPN(tokens)

def toRPN(s):

    tokens, stack = [], []
    number = ''

    for c in s:

        if c.isdigit():
            number += c
        else:
            if number:
                tokens.append(number)
                number = ''

            if c in operators:
                while len(stack) and getPriority(stack[-1]) >= getPriority(c):
                    tokens.append(stack.pop())
                stack.append(c)


            elif c == '(':
                stack.append(c)

            elif c == ')':
                while len(stack) and stack[-1] !='(':
                    tokens.append(stack.pop())
                stack.pop() 

    if number:
        tokens.append(number)

    while len(stack):
        tokens.append(stack.pop())

    return tokens

def evalRPN(tokens):

    operands = []
    for token in tokens:
        if token in operators:
            y,x = operands.pop(), operands.pop()
            operands.append(getVal(x,y,token))
        else:
            operands.append(int(token))

    return operands[0]

def getVal(x, y, operator):

    return {
        '+' : lambda x, y: x + y,
        '-' : lambda x, y: x - y,
        '*' : lambda x, y: x * y,
        '/' : lambda x, y: x / y
    }[operator](x,y)    

def getPriority(operator):

    return {
        '+' : 1,
        '-' : 1,
        '*' : 2,
        '/' : 2

    }.get(operator, 0)


print calculate("3+2*2")
print calculate("(1+(4+5+2)-3)+(6+8)")

