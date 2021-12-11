amt=int(input("enter the number:"))
note500=note200=note100=note50=note20=note10=note5=note2=note1=0
if amt>=500:
    note500=amt//500
    amt=amt-note500*500
    print("500=",note500)
elif amt>=200:
    note200=amt//200
    amt=amt-note200*200
    print("200=",note200)
elif amt>=100:
    note100=amt//100
    amt=amt-note100*100
    print("100=",note100)
elif amt>=50:
    note50=amt//50
    amt=amt-note50*50
    print("50=",note50)
elif amt>=20:
    note20=amt//20
    amt=amt-note20*20
    print("20=",note20)
elif amt>=10:
    note10=amt//10
    amt=amt-note10*10
    print("10=",note10)
elif amt>=5:
    note5=amt//5
    amt=amt-note5*5
    print("5=",note5)
elif amt>=2:
    note2=amt//2
    amt=amt-note2*2
    print("2=",note2)
elif amt>=1:
    note1=amt//1
    amt=amt-note1*1
    print("1=",note1)
else:
    print("0=",0)




