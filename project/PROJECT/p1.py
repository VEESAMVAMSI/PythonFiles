import csv
f=open("Amazon.csv","a",newline="")
a=csv.writer(f)

a.writerow(["user","password"])
user=(input("Enter username:"))
pwd=int(input("Enter your ph no:"))
a.writerow([user,pwd])
print("record saved succesfully")
