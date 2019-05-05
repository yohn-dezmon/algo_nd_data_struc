# this converts a number into it's hexadecimal... or if you have a base of 2 to binary
# or if you have a base of 10, decimal...
def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(10,16))

# toStr(10,2)
# toStr(5, 2) + convertString[0]
# ... toStr(2, 2) + convertString[1]
# ... toStr(0,2)
