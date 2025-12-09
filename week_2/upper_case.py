try:
    with open("message.txt") as file:
        line=file.read()
        line.upper()
        print(line.upper())
except FileNotFoundError:
    print("File does not exist")