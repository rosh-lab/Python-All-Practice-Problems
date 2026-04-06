#Program for finding biggest of two numbers by using ternary operator
#BiggestTwoEx1.py
a=float(input("Enter first value:"))
b=float(input("Enter second value:"))
print("*"*50)
#logic for biggest number
var=a if a>b else b
print("Big value({},{})={}".format(a,b,var))
