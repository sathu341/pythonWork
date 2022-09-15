#0,1,1,2,3,5,8

print("Limite number")
l=int(input())
a=0
b=1
print("0,1",end=",")
while l>0:
    c=a+b
    print(c,end=",")
    a=b
    b=c
    l-=1
    
