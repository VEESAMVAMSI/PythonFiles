n=int(input("num:"))
count=0
num=0
while(n>0):
    num=n%10
    count+=1
    n=n//10
print(count)