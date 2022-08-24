class Bike():
    def __init__(self,bm,cmp,clr,prc):
        self.modelName,self.company,self.color,self.price=bm,cmp,clr,prc

    def getDetail(self):
        print(f'Model Name:{self.modelName}\n Company:{self.company}\n Color:{self.color},Price:{self.price} ')


bk=Bike("Bajaj456","Bajaj","Black",85000)     
bk.getDetail()       