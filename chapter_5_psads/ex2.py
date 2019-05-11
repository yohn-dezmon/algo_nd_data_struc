# Use the binary search functions given in the text (recursive and iterative).
# Generate a random, ordered list of integers and do a benchmark analysis for
# each one. What are your results? Can you explain them?

# Binary recursive time is consistently less efficient... why?
# I think the reason why the recursive function is slower is because
# with each call of the binarySearch_rec, you have to slice the list which is
# expensive in terms of time.
# I think with the other function (non-recursive), you are continually analyzing
# different areas of the SAME list :D

import random
import timeit
# non recursive!
def binarySearch(alist, item):
	    first = 0
	    last = len(alist)-1
	    found = False

	    while first<=last and not found:
	        midpoint = (first + last)//2
	        if alist[midpoint] == item:
	            found = True
	        else:
	            if item < alist[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1

	    return found

# recursive!
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

# generating random list
# list_of_int = random.sample(range(10000,50000), 20)
# generating random number to search for
# random_num = random.randint(10000,50000)


def binary_time():
    Setup_Code = """
from __main__ import binarySearch
import random
    """

    Test_Code = """
list_of_int = [x for x in range(9999)]
look_fer = random.randint(0,len(list_of_int))
binarySearch(list_of_int, look_fer)
    """

    # time it !!!
    times = timeit.repeat(stmt = Test_Code,
                          setup = Setup_Code,
                          repeat = 3,
                          number = 10000)
    print(f"Binary time: {min(times)}")

def binary_rec_time():
    Setup_Code = """
from __main__ import binarySearch_rec
import random
    """

    Test_Code = """
list_of_int = [x for x in range(9999)]
look_fer = random.randint(0,len(list_of_int))
binarySearch_rec(list_of_int, look_fer)
    """

    # time it !!!
    times = timeit.repeat(stmt = Test_Code,
                          setup = Setup_Code,
                          repeat = 3,
                          number = 10000)
    print(f"Binary recursive time: {min(times)}")


if __name__ == "__main__":
    binary_time()
    binary_rec_time()
