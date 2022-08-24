from re import A


def addFunction(x,y):
    ans=x+y
    return ans

# result=addFunction(4,5)    
# print(result)

def Calu(opr,n1,n2):
    if opr=="+":
        result=n1+n2
    elif opr=="-":
        result=n1-n2
    elif opr=="*":
        result=n1*n2
    elif opr=="/":
        result=n1/n2

    return result      


print("+,-,*,/ select your option")          
opr=input()
print("Enter the first no")
x=float(input())
print("Enter the second no")
y=float(input())
ans=Calu(opr,x,y)
print("Result ",ans)
