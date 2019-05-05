# palindrome > same forwards + backwards
# therefore given a string I need to reverse it, get its value, then say does string vs. reversed = ?

# from test import testEqual
def removeWhite(s):
    if len(s) <= 1:
        return s
    elif s[0] == " ":
        return removeWhite(s[1:])
    else:
        return s[0] + removeWhite(s[1:])


    return s

def isPal(s):
    def reverse_Str(s):
        if len(s) <= 1:
            return s
        else:
            return s[-1] + reverse_Str(s[:-1])

    if s == reverse_Str(s):
        return True
    else:
        return False

# testEqual(isPal(removeWhite("x")),True)
# testEqual(isPal(removeWhite("radar")),True)
# testEqual(isPal(removeWhite("hello")),False)
# testEqual(isPal(removeWhite("")),True)
# testEqual(isPal(removeWhite("hannah")),True)
# testEqual(isPal(removeWhite("madam i'm adam")),True)

print(isPal("kayak"))

print(isPal(removeWhite("bob bob")))
