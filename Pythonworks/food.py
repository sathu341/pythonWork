class food():
    def stdata(self):
        self.name=input("enter the food name")
        self.price=int(input("enter the rate"))
    def dis(self):
        print(self.name)
        if self.price>150:
            self.dis=(self.price*10)/100
            self.price=self.price-self.dis
            print(self.price)
        else:
            print (self.price)
obj=food()
obj.stdata()
obj.dis()
