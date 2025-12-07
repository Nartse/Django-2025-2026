num=int(input("Input n= "))
n=[]
for i in range (1,num+1):
    if i%3==0 and i%5==0:
        n.append("FizzBuzz")
    elif i%3==0:
        n.append("Fizz")
    elif i%5==0:
        n.append("Buzz")
    else:
        n.append(i)
print("Output: ",n)