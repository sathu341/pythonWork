class mobile():
    def setdata(self):
        self.name=input("enter the name")
        self.model=input("enter the model")
        self.price=int(input("enter the price"))
        self.company=input("enter the company")
        if self.company=="":
            print("phone")
        else:
            print(self.company)
    def display(self):
        print(self.name)
        print(self.model)
        print(self.price)
        print(self.company)
obj=mobile()
obj.setdata()
obj.display()

