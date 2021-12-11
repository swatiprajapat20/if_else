time = float(input("enter the schedual:"))
if (time>=6) and (time<=7):
    print("morning excercise")
elif (time>=7) and (time<=8):
    print("bathing")
elif (time>=8) and (time<=9):
    print("breakfast")
elif (time>=9) and (time<=12-30):
    print("coding")
elif (time>=12-30) and (time<=14):
    print("lunch break")
elif (time>=14) and (time<=17):
    print("coding")
elif (time>=17) and (time<=18):
    print("culture activity")
elif (time>=18) and (time<=18-30):
    print("snacks break")
elif (time>=18-30) and (time<=20):
    print("coding")
elif (time>=20) and (time<=21):
    print("english activity")
elif (time>=21) and (time<=22):
    print("dinner time")
else:
    ("sleeping")