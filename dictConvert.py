
def setData(limit):
    number=[]
    name=[]
    for i in range(limit):
        print("enter name")
        name.append(input())
        print("enter  number")
        number.append(input())
    return name,number    

def convertDict(k,v):
    dc=zip(k,v)    
    dc=dict(dc)
    return dc
def display(data):
    for k in data:
        print(k,data[k])   
while(True):
    if ans=="n":
        break
    l=int(input("Enter the  limit"))    

    k,v=setData(l)
    data=convertDict(k,v)
    display(data)

    print("Do u want to continue?y/n")
    ans=input()
    ans=ans.lower()
    if ans=="n":
        break
    if ans!="y" or ans!="n":
        print(" Enter  n to  quite or y to continue")
        ans=input()
        ans=ans.lower()






