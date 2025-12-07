num=int(input("Enter a number to know if it is palindrome or not: "))
reversed_num=0
original_num=num
while num>0:
    digit=num%10
    reversed_num=reversed_num*10+digit
    num=num//10
if original_num==reversed_num:
    print("true")
else:
    print("false")