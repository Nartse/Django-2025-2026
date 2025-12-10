class Student:
    def set_grade(self,grade):
        self.__grade=grade
    def get_grade(self):
        return self.__grade
s1= Student()
s1.set_grade("A")
print("Grade:",s1.get_grade())