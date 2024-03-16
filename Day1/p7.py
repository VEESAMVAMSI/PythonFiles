# a=int(input("n1"))
# b=int(input("n2"))
# c=int(input("n3"))
# if a==b==c:
#    print("equ")
# elif a==b or b==c:
#    print("iso") 
# else:
#    print("sca")

# factorial=1
# for i in range(1,8):
#     factorial=factorial*i
# print(factorial)
# n1=0
# n2=1
# n3=0
# for i in range(2, 11):
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     print(n3)
a=int(input("num"))
flag=0
for i in range(2,a):
    if a%i==0:
       flag=1
if flag==1:
    print("not a prime num")
else:
    print("prime")



