from pythonds.basic import Stack

def infixToPostfix(infixexpr):
    prec = {} # this dictionary assigns each operator a precedence value!
    prec["**"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = [] # list that the postfix values will be added to after being put in the stack
    tokenList = infixexpr.split() # if two characters are together without spaces, they will be
    # represented as one token! :D

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(': # ok this is key! the ('s  are not added to the final list! :D
                postfixList.append(topToken)
                topToken = opStack.pop()

        # elif (not opStack.isEmpty()) and \
        #    (opStack.peek() == token) and token == "*" and tokenlist[token] + 1 == "*":
        #    opStack.push(token+"*")
        # elif (not opStack.isEmpty()) and \
        #    (opStack.peek() == token) and token == "*" and tokenlist[token] - 1 == "*":
        #    pass
        # elif (not opStack.isEmpty()) and \
        #    (opStack.peek() == token) and token == "*" and tokenlist[token] + 1 != "*":
        #    opStack.push(token)
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
              postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

# print(infixToPostfix("A * B + C * D"))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))


print(infixToPostfix("5 * 3 ** ( 4 - 2 )"))
# postfix >> 5 3 4 2 - ** * ...
# >> 5 3 2 **   THIS IS NON COMUTATIVE
# >> 5 9 *
# >> 45



# final example
# 5 gets passed to postfixList
# * gets put into the stack
# 3 gets passed to post fix list
# the second * would trigger the new code, HMMM how can I distinguish this from ** ?


# example 1:
# A >> gets passed into the postfixList
# * >> goes to else, breaks the while loop, then opStack.push(token) pushes it to the stack.
# B >> gets passed into the postfixList
# + >> prec[opStack.peek()] IS >= to prec[+] so * gets added to postfixList
# then + gets added to the stack
# C is added to postfixList
# * is > than + so while loop is broken and * is added to the stack
# D is added to post fix list
# then the next while loop is started, b/c the stack isn't empty
# the contents of the stack are emptied using pop, releasing the top to the bottomself.
# the contents of the list are joined together using .join

# how does the first operator get added? ah this would evaluate to false and break the while loop.
