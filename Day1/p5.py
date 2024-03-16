a=72000
income=0
insur=0
total=0
b=int(input("p:"))
if b>a and b<150000:
    income=b*10//100
    ins=b*15//100
    total=b+income+insur
    print(total)
elif b>150000 and b<200000:
    income=b*25//100
    ins=b*20//100
    total=b+income+insur
    print(total)
elif b>200000:
    income=b*35//100
    ins=b*28//100
    total=b+income+ins
    print(total)
else:
    print("enter valid num")



