student={"nardos":"A","abebe":"B","abel":"B+","lina":"C"}
name=input("Student Name: ")

def get_grade(student_grades, student_name):
    try:
        return student_grades[student_name]
    except KeyError:
        print("Student not found in a system")
print(get_grade(student,name))