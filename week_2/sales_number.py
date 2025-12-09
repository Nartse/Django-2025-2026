sales=[]
with open("sales.txt","r") as file:
    for line in file:
        try:
            number=int(line)
            sales.append(number)
        except ValueError:
            print("Invalid, skipped")
    total=sum(sales)
print("Valid sales numbers: ",sales)
print("Total sales: ",total)