numbers=[]
with open("numbers.txt") as file:
    for line in file:
        try:
            num=int(line)
            numbers.append(num)
        except ValueError:
            print("Invalid line, Ignored")
sum=sum(numbers)
print("Sum: ",sum)
