#Swapping logic for single line assignment
#For swapping any two integer values
a,b=int(input("Enter value of a:")),int(input("Enter value of b:"))
print("*"*50)
print("Original value of a {}".format(a))
print("Original value of b {}".format(b))
print("*"*50)
#swapping logic
a=a*b
b=a//b
a=a//b
#or a=a+b
#   b=a-b
#   a=a-b
print("Swapped value of {}".format(a))
print("Swapped value of {}".format(b))
