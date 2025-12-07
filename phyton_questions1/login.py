with open("log.txt", "w") as file:
    file.write("User logged in")
with open("log.txt","r") as file:
    content=file.read()
    print(content)