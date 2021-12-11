num=int(input("enter the number(1-6):"))
if num==1:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    c=a+b
    print("add=",c)
elif num==2:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    c=a-b
    print("substrate=",c)
elif num==3:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    c=a*b
    print("multiply=",c)
elif num==4:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    c=a/b
    print("divide=",c)
elif num==5:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    c=a%b
    print("modulus=",c)
elif num==6:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    c=a//b
    print("floor division=",c)
else:
    print("invalid ")
