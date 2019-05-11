# Implement the binary search using recursion without the slice operator.
# Recall that you will need to pass the list along with the starting and ending
# index values for the sublist. Generate a random, ordered list of integers and
# do a benchmark analysis

# RESULTS: yay! as predicted, the binary search without slices is faster! :D 
# Even though a binary search is generally better than a sequential search,
# it is important to note that for small values of n, the additional cost of sorting
# is probably not worth it.


import random
import timeit

def binarySearch(alist, term, start, ultimo):
    found = False

    while start <= ultimo and not found:
        midpoint = (ultimo+start)//2
        if term == alist[midpoint]:
            found = True
            return found
        else:
            if term > alist[midpoint]:
                return binarySearch(alist, term, midpoint+1, ultimo)
            else:
                return binarySearch(alist, term, start, midpoint-1)

    return found

def binarySearch_rec(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
          return True
        else:
          if item<alist[midpoint]:
            return binarySearch_rec(alist[:midpoint],item)
          else:
            return binarySearch_rec(alist[midpoint+1:],item)



# list1 = [1,2,3,4,5,6]
# index_len = len(list1)-1
# print(binarySearch(list1, 6, 0, index_len))


def binary_search():
    Setup = """
from __main__ import binarySearch
import random
"""

    Stmt = """
rando_list = [random.randint(1,10000) for x in range(20)]
rando_list.sort()
index_len = len(rando_list)-1
look_fer = random.randint(1,10000)
binarySearch(rando_list, 1500, 0, index_len)
"""

    times = timeit.repeat(stmt = Stmt,
                  setup = Setup,
                  repeat = 3,
                  number = 10000)
    print(f"No Slice Recursive Binary Search: {min(times)}")

def binary_rec_time():
    Setup_Code = """
from __main__ import binarySearch_rec
import random
    """

    Test_Code = """
rando_list = [random.randint(1,10000) for x in range(20)]
rando_list.sort()
look_fer = random.randint(1,10000)
binarySearch_rec(rando_list, look_fer)
    """

    # time it !!!
    times = timeit.repeat(stmt = Test_Code,
                          setup = Setup_Code,
                          repeat = 3,
                          number = 10000)
    print(f"Binary recursive time: {min(times)}")

if __name__ == "__main__":
    binary_search()
    binary_rec_time()
