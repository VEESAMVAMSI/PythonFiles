#take an integer as an input from user and check whether if the num is divisible by sum of digits-21
n=int(input("num:"))
sum=0
n1=n
while(n>0):
    digit=n%10
    sum+=digit
    n=n//10
print(sum)

if n1%sum==0:
    print("yes")
else:
    print("no")
