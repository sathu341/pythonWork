class Hero():
    def  info_hero(self):
        print("Hero Class")

class Honda():
    def  info_Honda(self):
        print("Honda")


class HeroHonda(Hero,Honda):
    def inf_herohonda(self):
        print("Hero Honda")

obj=HeroHonda()
obj.info_hero()
obj.info_Honda()
obj.inf_herohonda()        