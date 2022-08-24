class Book():
    'the class is for the  book  objects'
    title=""
    price=0

    def setTitle(self,t):
        self.title=t
       
    def getTitle(self):
        print("Book Title:",self.title)    

    def setPrice(self,prc):
        self.price=prc

    def getPrice(self):
        print("Book Price:",self.price)   

#Object create 
alice=Book()
alice.setTitle("Alice in  Wonderland")         
alice.setPrice(564)
alice.getTitle()
alice.getPrice()