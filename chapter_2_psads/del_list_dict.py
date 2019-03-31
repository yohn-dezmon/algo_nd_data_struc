from timeit import Timer


# Devise an experiment that compares the performance of the del operator on lists and dictionaries

def makelist(n):
    x = list(range(n))
    return x

def dellist(x):
    del x[0]

print("Experiment showing that del x[0] is O(n)")
t1 = Timer("dellist(x)", "from __main__ import makelist, dellist; x = makelist(200)")
print(t1.timeit(number=200))
t2 = Timer("dellist(x)", "from __main__ import makelist, dellist; x = makelist(400)")
print(t2.timeit(number=200))
t3 = Timer("dellist(x)", "from __main__ import makelist, dellist; x = makelist(800)")
print(t3.timeit(number=200))

print("""

""")
print("Experiment showing that del operator on dictionaries is O(1) regardless of size")


#chr(97) is equal to a! :D chr(65) is equal to A! :D
# dict comprehension format >>> {i: (chr(65+i) for i in range(4)}
# The reason why I'm getting keyerror: 0 >>> https://stackoverflow.com/questions/36418946/python-key-error-when-using-timeit-to-test-dictionary-key-deletion-time

# from keys >>> two parameters (1) sequence: sequence of elements which is to be used as keys for the new dictionary.
#  (2) value (opt) value which is set to each element of the dictionary ...

# explains the underscore: https://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python

# iter is typically used in conjunction with next()
# you set a variable equal to an iter object
# then you call next(iter_object)

def make_dict(n):
    x = {i : chr(65+i) for i in range(n)}
    return x

x = make_dict(10)
y = make_dict(5)

def delete_dict(x):
    try:
        del x[0]
    except KeyError:
        x.setdefault(0, None)
        del x[0]


t4 = Timer("delete_dict(y)", "from __main__ import make_dict, delete_dict, y;")
print(t4.timeit(number=200))
t5 = Timer("delete_dict(x)", "from __main__ import make_dict, delete_dict, x;")
print(t5.timeit(number=200))
