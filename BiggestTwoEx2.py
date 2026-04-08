#Program for finding biggest of two numbers and check for equality by using ternary operator
#BigggestTwoEx2.py
a=float(input("Enter first value:"))
b=float(input("Enter second value:"))
#logic for equality
#nested ternary operator
res=a if a>b else b if b>a else "Both values are equal"
print(" Biggest Value({},{})={}".format(a,b,res))