# Set up a random experiment to test the difference between a sequential search
# and a binary search on a list of integers.

# how to measure the time a function takes? use "timeit" module
import timeit
import random


def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1

        return found


def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
          return True
        else:
          if item < alist[midpoint]:
            return binarySearch(alist[:midpoint], item)
          else:
            return binarySearch(alist[midpoint+1:], item)

testlist = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
print(binarySearch(testlist, 16))

def binary_time():
    Setup_Code = """
from __main__ import binarySearch
from random import randint
    """

    Test_Code = """
testList = [x for x in range(9999)]
look_fer = randint(0,len(testList))
binarySearch(testList, look_fer)
    """

    # time it !!!
    times = timeit.repeat(stmt = Test_Code,
                          setup = Setup_Code,
                          repeat = 3,
                          number = 10000)
    print(f"Binary time: {min(times)}")


def Linear_time():
    Setup_Code = """
from __main__ import sequentialSearch
from random import randint
"""

    Test_Code = """
testList = [x for x in range(9999)]
look_fer = randint(0,len(testList))
sequentialSearch(testList, look_fer)
"""

    times = timeit.repeat(stmt = Test_Code,
                          setup = Setup_Code,
                          repeat = 3,
                          number = 10000)
    print(f"Sequential time: {min(times)}")





if __name__ == "__main__":
    binary_time()
    Linear_time()
