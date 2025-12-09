num=int(input("How many no of lists: "))
number=[]
for i in range(1,num+1):
    n=int(input("Enter a number: "))
    number.append(n)
max_num=number[0]
for n in number:
    if n>max_num:
        max_num=n
print("List: ",number)
print("The maximum number is: ", max_num)
