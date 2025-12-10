class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def annual_salary(self):
        self.annual=12*self.salary
        return self.annual
e=Employee("Nardos",10000)
print("Name:",e.name,",Annual salary:",e.annual_salary())