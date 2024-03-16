#calculate the difference of sum of nums divisible by six and not divisible by six in range of <30

i=1
max=0
min=0
while(i<=30):
    if i%6==0:
        max=max+i
    elif(i%6!=0):
        min=min+i
    i=i+1      
print(min-max)