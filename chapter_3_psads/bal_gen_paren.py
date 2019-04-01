from pythonds.basic import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol): # this takes the s.pop and makes it the open..
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
        opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))

# Second example:
# [ into stack
# { into stack
# ( into stack
# ) removes (
# ] goes to else, results in { getting popped off
# matches({,]) > returns 3 != 2 ... that's interesting I've never seen
# .index comparing a value of a character based upon an already setup list of characters...
# balanced gets set to false ...
# while loop completes
# False is returned :D 

