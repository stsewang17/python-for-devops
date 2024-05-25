import sys

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

def add(num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):
    sub = num1 - num2
    return sub

def mul(num1, num2):
    mul = num1 * num2
    return mul

def div(num1, num2):
    div = num1 / num2
    return div

if operation == "add":
    output = add(num1, num2)
    print(output)
elif operation == "sub":
    output = sub(num1, num2)
    print(output)
elif operation == "mul":
    output = mul(num1, num2)
    print(output)
elif operation == "div":
    output = div(num1, num2)
    print(output)
