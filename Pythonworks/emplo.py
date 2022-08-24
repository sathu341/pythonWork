class employee():
    def setData(self,nm,dg,dp,s):
        self.name=nm
        self.desig=dg
        self.dep=dp.lower()
        if(self.dep=="trainee"):
            self.salary=5000
        else:
            self.salary=s    
    def getData(self):    
        print(self.name,self.desig,self.dep,self.salary)

obj=employee()
obj.setData("jose","developer","Trainee",35000)
obj.getData()

