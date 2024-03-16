n=int(input("nums:"))
sum=0
count=0
while(n>0):
    count=count+1
    n=n//10
rev=0
a=153
while(a>0):
    digit=a%10
    rev+=digit**count
    a=a//10
if(rev==a):
    print("armstrong")
else:
    print("not armstrong")
