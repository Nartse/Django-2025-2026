prices = [120, 45, 300, 85, 150]
def get_expensive_products():
    result=[]
    for i in range(len(prices)):
        if prices[i]>100:
            result.append(prices[i])
    return result
print(get_expensive_products())