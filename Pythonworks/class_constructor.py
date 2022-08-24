class Book():
    bname=""
    price=0

    #constructor
    def __init__(self,bnam="jill",prc=0):
        self.bname,self.price=bnam,prc
        
    def getBname(self):
        return self.bname
    def getPrice(self):
        return self.price



b=input("Enter the Book Name")
p=float(input("Enter the Book Price"))

b1=Book(b,p)
print("Book Name",b1.getBname())
print("Price",b1.getPrice())