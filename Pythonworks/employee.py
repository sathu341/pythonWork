class employee():
    def name(self):
        self.a=input("enter the name :\t")
    def dep(self):
        self.b=input("enter the department :\t")
    def des(self,num):
        print(self.num==1,"1 . other")
        print(self.num==2,"2 . trainee")
        self.num=int(input("enter the designation number :\t"))
    def sal(self,sal,num):
        if self.num==1:
            print("salary of",self.a,"is 10000")
        elif self.num==2:
            print("salary of",self.a,"is 5000")
        else:
            print("invalid designation number")
obj=employee()
obj.name()
obj.dep()
obj.des()
obj.sal()
