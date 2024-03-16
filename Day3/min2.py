
lis=[22,42,65,0,1,-4,6,-1]
min1=lis[0]
min2=lis[0]
for i in lis:
    if i<min1:
        min2=min1
        min1=i

 
print(min1)
print(min2)