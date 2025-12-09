n=int(input("How many lists: "))
nums=[]
non_zero=0
for i in range(n):
    numbers=int(input("Enter numbers: "))
    nums.append(numbers)
for i in range(n):
    if nums[i]!=0:
        nums[non_zero]=nums[i]
        non_zero=non_zero+1
for i in range(non_zero,n):
    nums[i]=0
print(nums)