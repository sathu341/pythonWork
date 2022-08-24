#multiplies=> interface=>,abstract class abstract method
from abc import ABC,abstractmethod
class TataTeasouth(ABC):
    @abstractmethod 
    def address(self):
        print("south")

class TataTeaNorth():
    @abstractmethod
    def address(self):
       print("north")

class TataTeaProduct1(TataTeasouth,TataTeaNorth):
    def address(self):
        print("Moonar Tata Ripple .pvt.ltd")
class TataTeaProduct2(TataTeasouth,TataTeaNorth):
    def address(self):
        print("wynnad Tata Ripple .pvt.ltd")        
      
obj=TataTeaProduct1()
obj.address()

obj1=TataTeaProduct2()
obj1.address()

