class anim():
    def setdata(self,nam,ml,fd):
        self.name=nam
        self.max_life=ml
        self.food=fd
    def dis(self):
        print(self.name)
        print(self.max_life)
        print(self.food)
obj=anim()
obj.setdata("monkey","15","fruits")
obj.dis()
