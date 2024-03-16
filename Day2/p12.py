n=int(input('num:'))
rev=0
n1=n
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if n1==rev:
    print("palindrome")
else:
    print("not palindrome")