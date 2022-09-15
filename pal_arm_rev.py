print("Enter the no")
no=input()
org=no
rev=no[::-1]
print("Reverse:",rev)

if (org==rev):
    print("palandrome")
else:
    print("not palandrome")

#153   is a armstrong number  
n2=input("Enter no to  check armstrong or not")
s=0
for n in n2:
    s=s+(int(n)**3)
num=int(n2)
if s==num:
    print("Armstrong")
else:
    print("Not Armstrong")    