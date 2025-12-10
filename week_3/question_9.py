class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def display(self):
        print("Brand:",self.brand,",Year:",self.year)
class Car(Vehicle):
    def __init__(self,brand,year,model):
        super().__init__(brand,year)
        self.model=model
    def display2(self):
        print("Brand:",self.brand,",Year:",self.year,",Model",self.model)
v=Vehicle("Toyota",2005)
v.display()
c=Car("Toyota",2005,9)
c.display()
c.display2()