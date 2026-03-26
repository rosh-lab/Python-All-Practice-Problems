#Program which will accept length and breadth and calculate area of rectangle and its perimeter.
length=float(input("Enter length:"))
breadth=float(input("Enter breadth:"))
recarea=length*breadth
perimeter=2*(length+breadth)
print("Area of rectangle ({},{})={}".format(length,breadth,recarea))
print("Perimeter = {}".format(perimeter))