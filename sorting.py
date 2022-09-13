a=[2,7,6,5,1,10]
l=len(a)
print("befor sort")
print(a)
for i  in range(l):
    for j in range(l):
        if a[i]>a[j]:
            temp=a[j]
            a[j]=a[i]
            a[i]=temp
print("After sort")
print(a)
print("Second largest ",a[1])


