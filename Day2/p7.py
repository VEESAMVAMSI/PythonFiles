n=int(input("num:"))
num=0
sum=0
while(n>0):
    num=n%10
    sum+=num 
    n=n//10
print(sum)