# n from user check if the sum of factors of that num is greater than the original num or not
# n=int(input("nums:"))
# i=1 
# sum=0
# n1=n
# while(n>0):
#     if(n%i!=0):
#         i+=1
#     else:
#         sum+=i
# print(sum)
n=int(input("nums:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
if sum>n:
    print("yes")
else:
    print("no")