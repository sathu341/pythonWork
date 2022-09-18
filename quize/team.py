class Team():
    #constructor
    def __init__(self,id,nm):
        self.__iteamid=id
        self.iteam_name=nm
        self.Point=0
        try:
            self.fw=open('datastore.txt','a')
        except Exception as e:
            print(e)    
    #method
    def addPoint(self):
        self.Point+=1
    
    def subPoint(self):
        self.Point-=1
    def display(self):
        x="iteam id: "+str(self.__iteamid)+"\n"
        self.fw.write(x)
        y="iteam Name: "+self.iteam_name+"\n"
        self.fw.write(y)
        self.fw.write("Point:"+str(self.Point)+"\n")
        print("Team Id:",self.__iteamid) 
        print("Team Name:",self.iteam_name)
        print("POint:",self.Point)
