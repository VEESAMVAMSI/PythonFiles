# ms={1,2,.3,4+5j,True,"String"}

# print(ms.update([9,8,7,6]))
# #.remove.add
lis=[0,0,0,4]
nz=0
z=0
while nz<len(lis):
    if lis[nz]!=0:
        temp=lis[nz]
        lis[nz]=lis[z]
        lis[z]=temp
        nz=nz+1
        z=z+1
    else:
        nz=nz+1 
print(lis)