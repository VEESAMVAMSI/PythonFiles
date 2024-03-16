y=int(input("year:"))
# if a%4==0 and a%100!=0:
#     print("it is a leap year")
# elif a%400==0:
#     print("it is a leap year")
# else:
#     print("not leap year")
if (y%4==0 and y%100!=0) or y%400==0:
   print("it is leap year")