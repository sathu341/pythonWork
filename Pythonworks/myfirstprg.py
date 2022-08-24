class Pen:
    def __init__(self,idn):
        self.idno=idn
    def getData(self):
        print("idno",self.idno)



parker=Pen(234)

inkpen=Pen(567)

print("Parker",parker.getData()) #1101
print("inkpen",inkpen.getData()) #00101

