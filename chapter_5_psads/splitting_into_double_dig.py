# This script takes a large integer, and splits it into two digit pairs. 
# this will be used in the implementation of a fold-method for creating a hash table! 

n = 1234567891

# convert the integer to a list of individual strings/characters ['1','2'...]
nstr = str(n)

# make a list of integers, this was necessary for line 14... 
nint = [int(i) for i in nstr]


# the enumerate function allows you to access the index of each item in the list, as well as the value 
for indx, val in enumerate(nint):
    plus1 = indx + 1
    # I had to make this if condition, b/c it would throw an error if I tried to call an index that didn't exist
    if plus1 in range(len(nint)):
        nint[indx] = str(nint[indx]) + str(nint[plus1])
        del nint[plus1]         # I had to delete the second number in the pair after adding it to the first so it wouldn't be 
                                # added again to the third element in the list 

# convert the double digit pairs to integers 
nint = [int(i) for i in nint]

print(nint)
