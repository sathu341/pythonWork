from ast import Pass


a=[1,7,6,7,1]
l=len(a)
count=0
dup=[]
print("befor sort")
print(a)
for i  in range(l):
    for j in range(l):
        if i!=j:
           if a[i]==a[j]:
                if j in dup:
                    pass
                else:
                  dup.append(j)
              


for ls in dup:
    print(a[ls])
dup1=[]
for  l in a:
    cnt=a.count(l)
    if cnt>1:
        if  l in dup1:
          pass
        else:
          dup1.append(l)
print(dup1)        


              

