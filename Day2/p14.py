n=int(input("nums:"))
count=0
while(n>0):
    count=count+1
    n=n//10
rev=0
a=1578
while(a>0):
    digit=a%10
    rev+=digit**count
    a=a//10
    count=count-1
print(rev)

