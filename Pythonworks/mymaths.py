from  mymodules import mathspage




M=mathspage.Maths()
ch=M.menu()
no=[]
if(ch==1):
    print("enter  count of number")
    l=int(input())
    for n in range(l):
        print("Enter no")
        no.append(input())

    print(M.addno(no))
if(ch==2):
    print("enter  count of number")
    l=int(input())
    for n in range(l):
        print("Enter no")
        no.append(input())

    print(M.multi(no))    
if(ch==3):
    print("enter  Radius value")
    r=int(input())
    print('Circle Area:',M.circleArea(r))
if(ch==4):
    print("enter  Length  of the Rectangle")
    l=int(input())
    print("enter  Breadth  of the Rectangle")
    b=int(input())
    print('Rectangle Area:',M.rectArea(l,b))    
