#6n=int(input("num"))
# flag=0
# for i in range(2,a):
#     if a%i==0:
#        flag=1
# if flag==1:
#     print("not a prime num")
# else:
#     print("prime")
n = int(input("nums:"))
total_sum = 0
while n > 0:
    digit = n % 10
    total_sum += digit
    n //= 10
print("Sum of digits:", total_sum)