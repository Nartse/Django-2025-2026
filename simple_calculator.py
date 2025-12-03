num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print("+ =addition, - =subtraction, * =multiplication, / =division")
operation=input("Enter operation you want to perform: ")
def add():
    return num1+num2
def sub():
    return num1-num2
def mul():
    return num1*num2
def div():
    return num1/num2
if operation=="+":
    print(add())
elif operation=="-":
    print(sub())
elif operation=="*":
    print(mul())
elif operation=="/":
    print(div())
else:
    print("Wrong operation")