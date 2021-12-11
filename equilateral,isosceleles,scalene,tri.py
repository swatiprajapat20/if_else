x=int(input("enter the number:"))
y=int(input("enter the number:"))
z=int(input("enter the number:"))
if x==y==z:
    print("equilateral triangle")
elif x==y or y==z or z==x:
    print("isosceles triangle")
else:
    print("scalene triangle")




