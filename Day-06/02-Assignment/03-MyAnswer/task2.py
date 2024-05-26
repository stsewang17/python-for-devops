# Task 2: Comparison Operators

# 1. Compare the values of `a` and `b` using the following comparison operators: `<`, `>`, `<=`, `>=`, `==`, and `!=`.
# 2. Print the results of each comparison.


import sys

a = sys.argv[1]
operator = sys.argv[2]
b = sys.argv[3]

def lessthan(a, b):
    return a < b

def greaterthan(a, b):
    return a > b

def lessthanequal(a, b):
    return a < b

def greaterthanequal(a, b):
    return a < b

def equal(a, b):
    return a < b

def notequal(a, b):
    return a < b

if operator == "lessthan":
    print(lessthan(a, b))
elif operator == "greaterthan":
    print(greaterthan(a, b))
elif operator == "lessthanequal":
    print(lessthanequal(a, b))
elif operator == "greaterthanequal":
    print(greaterthanequal(a, b))
elif operator == "equal":
    print(equal(a, b))
elif operator == "notequal":
    print(notequal(a, b))

    
