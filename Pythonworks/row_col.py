r=int(input("enter row"))
c=int(input("enter row"))
rw=[]
cl=[]
for i in range(r):
    k=i

    for j in range(c):
        
        if i==0 and j==0:
            k=k+1
            print(k,end=",")
        elif i==r-1 and j==c-1:

             print(r*c,end=",")    
        else:
            if k==1:
                k=k+2
                print(k,end=",")
            elif j>1 and j<c:
                k=k+3
                print(k,end=",")    
    print()



