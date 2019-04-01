from pythonds.basic import Stack

def parChecker(symbolString):
    s = Stack() # initialize stack
    balanced = True # this will be used later
    index = 0 # initialize the index to 0
    while index < len(symbolString) and balanced: # symbol string, is a string of just parentheses.
        symbol = symbolString[index] # initializes a variable that is one character of the string
        if symbol == "(": # if it's an opening parenthesis, then it is added to the Stack...
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1 # this is called once the preceeding conditions are met...

    if balanced and s.isEmpty():
        return True
    else:
        return False

# Balanced Example:
# ((()))
# ( to the stack
# (( to the stack
# ((( to the stack
# ) causes the most recent ( to be removed from the stack
# ) causes the most recent ( to be removed from the stack
# ) causes the final ( to be removed from the stack
# the while loop completes, b/c index = len(symbolString)
# balanced is still true so the first if statement is processed
# the stack is empty so True is returned indicating that they match!

# Unbalanced example:
# ())
# ( is added to the stack
# ) causes ( to be removed from the stack
# at this point the stack is empty
# ) this goes to else, making balanced = False
# the while loop ends
# this goes to else, and returns false :D
