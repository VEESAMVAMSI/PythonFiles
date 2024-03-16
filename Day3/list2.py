# lis=[12,42,23,96,7,18,10,133]
# #add min and maxl

# min=lis[0]
# max=lis[0]
# for i in range(len(lis)):
#     if lis[i]<min:
#         min=lis[i]
#         min_i=i
#     if lis[i]>max:
#         max=lis[i]
#         max_i=i
# lis[min_i]=max-min
# lis[max_i]=max+min
# print(lis)


#lllllllll
#creation of tuple addding values manually and check the tuple are not
# tup=(1,2.3,45+6j,True,"String")
# #tup.append("False")
# tup=tup+("False",)
# print(tup)


#
# dic={'name':'vamsi','age':'22','month':'3','dob':'13'}
# print(dic)
# print(dic['age'])
# for key,value in dic.items():
#     print(key," ",value)
#[-1,42,65,1,-4,6]write a program  to find the second smallest negative number without using sort and min and max
lis=[22,-1,42,65,1,-4,6]
min1=999
min2=999
for i in lis:
    if i<min1:
        min1=i  
for i in lis:
        #or if i!=min1 and i<min2:
        if i>min1 and i<min2:
          min2=i
print(min2)
