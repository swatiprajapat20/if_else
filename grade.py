physics=int(input("enter the number:"))
chemistry=int(input("enter the number:"))
biology=int(input("enter the number:"))
mathematics=int(input("enter the number:"))
computer=int(input("enter the number:"))
total=physics+chemistry+biology+mathematics+computer
average=total/5
percentage=(total/500)*100
if percentage >=90:
    print("grade A")
elif percentage >=80:
    print("grade B")
elif percentage >=70:
    print("grade C")
elif percentage >=60:
    print("grade D")
elif percentage >=40:
    print("grade E")
else:
    print("grade F")












