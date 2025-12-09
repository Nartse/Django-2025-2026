num=int(input("Enter a number to calculate factorial: "))
def fact():
    factorial=1
    for i in range(1 , num+1):
        factorial*=i
    return factorial
print(fact())
