# reverse the digits using recursion
# def rev(n):
#     if(n==0):
#         return 
#     else:
#         print(n%10)
#         rev(n//10)
# rev(12345)
# writee the recursive fun to count the num of digits,sum of digits

# def num(n):
#     if(n==0):
#         return
#     else:
#         n=n%10
#         c=c+1
#         num(n//10)
#         num(12345)


# def num(n):
#     if(n==0):
#         return 0
#     else:
       
#         return n%10+num(n//10)
# print(num(3435)) 

# while(a>0):
#     digit=a%10
#     rev+=digit**count
#     a=a//10
def coun(n):
    if n==0:
        return 0
    else:
        return 1+coun(n//10)


def arm(s,p):
    if s==0:
        return 0
    else:
        return (s%10)**p+arm(s//10,p)
n=153
print("Number of digits:", coun(n))
print("Armstrong number:", arm(n,coun(n)))