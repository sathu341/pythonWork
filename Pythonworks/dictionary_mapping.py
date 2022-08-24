"""
dt={key:value,key:value}
flw={'R';'Rose','J':'jasmine'}
print(flw['R])
print(flw['J'])
zip()
"""
#phone book
name=[]
phone=[]
l=int(input("Enter the limit no of list"))
for i in range(l):
    n=input("enter the name")
    name.append(n)
    ph=input("enter the mobile number")
    phone.append(ph)

dt=zip(name,phone)    
dt=dict(dt)
print(dt)

