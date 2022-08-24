import math
class Arth():
    def addno(self,n):
        s=0
        for no in n:
            s=s+int(no)
        return s

    def multi(self,n):
        s=1
        for no in n:
            s=s*no
        return s

class Geo():
    def  circleArea(self,r):
        self.ar=(math.pi)*pow(r,2);
        return self.ar   

    def rectArea(self,l,b):
        self.ret=l*b
        return self.ret         

class Maths(Arth,Geo):
    def menu(self):
        print(f'1.Add\n2.Multiple\n3.Cricle Area\n4.Rectangle Area\n Choose Your option')
        self.ch=int(input())
        return self.ch







