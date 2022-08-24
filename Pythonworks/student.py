class Student():
    #class variable
    roll=0
    sname=""
    m1,m2,m3=0,0,0
    tot=0
    avg=0
    def setData(self,rl,nam,mr1,mr2,mr3):
        self.roll=rl
        self.sname=nam
        self.m1,self.m2,self.m3=mr1,mr2,mr3
    def getTotal(self):
        self.tot=self.m1+self.m2+self.m3
        return self.tot
    def getAverage(self):
        self.avg=self.getTotal()/3   
        return self.avg     

    def  showDetail(self):
        print("*****************Student Detail*********************\n")    
        print(f'Roll No:{self.roll}\n Name:{self.sname}\n Mark1:{self.m1} \n Mark2:{self.m2} Mark3:{self.m3}\n Total:{self.tot}\n Average:{self.avg}')
#****************************End  class*******************************************************************************

#object creation

ram=Student() 
ram.setData(1,'Ram',78,89,94)
tot=ram.getTotal()
print(f'Total mark:{tot}')
print(f'Average :{ram.getAverage()}')
ram.showDetail()