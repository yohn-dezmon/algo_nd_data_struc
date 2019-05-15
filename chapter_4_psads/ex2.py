# Write a recursive function to reverse a list.


def reverse_list(list1):
    reverselist = []
    if len(list1) <= 1:
        reverselist.append(list1[0])
        return reverselist
    else:
        reverselist.append(list1[-1])
        return reverselist + reverse_list(list1[:-1])

list1 = [1,2,3,4]
list2 = [5,6,7,8]

print(reverse_list(list1))
print(reverse_list(list2))

# THE REASON I WASN'T UNDERSTANDING THIS!
# I didn't understand reverselist + x b/c I didn't know what adding a list to
# anything else would do
# but you can add a list to another list, and what it does is combine the two lists
# and the indexing is such that the second list begins at the end of the first lists' index 
# list 1
# reverselist = [4]
# [4] + ... reverse_list([1,2,3])
# [4,3] + reverse_list([1,2])
# [4,3,2] + reverse_list([1])
# [4,3,2,1]
