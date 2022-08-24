class Tempature():
    def setdata(self,n):
       
        n=n[:-1]
        self.no=float(n)
    def cl_to_f(self):
        self.cl=((self.no*9)/5)+32
        return self.cl
    def f_to_cl(self):
        self.f=(self.no-32)*5/9
        return self.f


print("******************************convertor********************")
print("Menu\n1)Celius To Fahrenheit\n2)Fahrenheit To Celius \n Choose your option ?")
ch=int(input())

if ch==1:
    tmp=Tempature()
    x=input("Enter the celius ")
    tmp.setdata(x)
    print("Tempature convert to celius to Fahrenheit",tmp.cl_to_f(),"F")
elif ch==2:
     tmp2=Tempature()
     x=input("Enter the Fahrenheit ")
     tmp2.setdata(x)
     print("Tempature convert to  Fahrenheit to  celius ",tmp2.f_to_cl(),"C")
else:
    print("invalid entry ")
    
    
