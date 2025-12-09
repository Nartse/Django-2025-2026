x = int(input("Enter a non-negative integer: "))
result = 0
for i in range(x+1):
    if i * i <= x:
        result = i
    else:
        break

print("Integer square root:", result)
