n=int(input("num:"))
num=0
sum=1
while(n>0):
    num=n%10
    sum*=num 
    n=n//10
print(sum)