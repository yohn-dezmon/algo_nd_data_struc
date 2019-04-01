class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


# or you can just do from pythonds.basic import Stack

# write a function revstring(mystr) that uses a stack to reverse the characters in a stringself.

mystr = "Bicycle"
s = Stack()

def revstr(mystr):
    for chr in mystr: # takes each character of the string and makes it an item in the stack
        s.push(chr)
    bkwrds = [] # set up a list in which to add the pop'd items

    while s.size() > 0: # while the size of the stack is not 0
        x = s.pop() # you need to set s.pop() equal to a variable to store the value it returns 
        bkwrds.append(x) # the items are added to the new list, from last to first (LIFO) 

    bkwrds_str = ''.join(bkwrds) # this joins the items together into a singular string

    return bkwrds_str

print(revstr(mystr))
