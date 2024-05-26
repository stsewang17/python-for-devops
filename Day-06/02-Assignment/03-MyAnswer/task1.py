# ## Task 1: Arithmetic Operators

# 1. Create two variables `a` and `b` with numeric values.
# 2. Calculate the sum, difference, product, and quotient of `a` and `b`.
# 3. Print the results.

import sys

a = float(sys.argv[1])
operator = sys.argv[2]
b = float(sys.argv[3])

def add(a, b):
    add = a + b
    return add

def min(a, b):
    min = a - b
    return min

def mul(a, b):
    mul = a * b
    return mul

def div(a, b):
    div = a / b
    return div

if operator == "add":
    print(add(a, b))
elif operator == "min":
    print(min(a, b))
elif operator == "mul":
    print(mul(a, b))
elif operator == "div":
    print(div(a, b))