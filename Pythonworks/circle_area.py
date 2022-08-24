class Acompany:
 def address(self):
    print("Acompany Address")


class B(Acompany):
    def address(self):
        print("B Class Address")

b=B()
b.address()        