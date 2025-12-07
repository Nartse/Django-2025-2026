sentence=input("Enter a sentence: ")
words=sentence.split()
dictionary={}
for i in words:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
print(dictionary)