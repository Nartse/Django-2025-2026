scores = {"John": 85, "Sara": 92, "Fraol": 78}
name=input("Input a name of a student: ")
try:
    print(scores[name])
except KeyError:
    print("Student not found")