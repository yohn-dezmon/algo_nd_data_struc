# 1. Write a recursive function to compute the factorial of a number.

# three laws = 1. must be a base case
# 2. the state must change to reach teh base case
# 3. the function must call itself

# factorials: if you have 3! = 3 x 2 x 1
# or n! = n * n - 1 * n - 2 until n - x is <= 1
# we'll define factorial(0) = 1
# the number being subtracted is largest at (n-1)
# n! = n * n - 1 * n - 2 ... * (n-(n-1))

# base case is ... n <= 1
# base case is (n-(n-1))

def factorial(number):
    if number <= 1:
        return number
    else:
        return number * factorial(number - 1)





print(factorial(5))

# 3 ... 3 * ..
# 2 ... 2 * ...
# 1 (base case)
