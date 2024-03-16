a=int(input("n1"))
if a%3==0 and a%6==0:
    print("good number")
elif a%2 and a%7==0:
    print("avg num")
elif a%4==0 and a%9==0:
    print("awesome num")
else:
    print("bad num")
