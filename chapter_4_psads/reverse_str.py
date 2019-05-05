# write a recursive function that reverses a string
# base case ...
#

def reverse_Str(string):
    # I used <= to account for if the person enters a blank space! :D
    if len(string) <= 1:
        return string
    else:
        return string[-1] + reverse_Str(string[:-1])

print(reverse_Str("TALK"))


# reverse_Str("TALK")
# K + reverse_Str(TAL)
