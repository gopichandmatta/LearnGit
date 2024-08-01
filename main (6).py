list1=[1,2,3,2,3,4,5,6,3,7,8,5,4,9]
d={}
for i in list1:
    if i in d:
        d[i]+=1 
    else:
        d[i]=1 
print(d)