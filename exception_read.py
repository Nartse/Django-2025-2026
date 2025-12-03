try:
    with open ("nardos.txt", "w") as file:
        file.write("Welcome, Nardos")
    with open ("nardos.txt") as file:
        file.read("nardos.txt")
except FileNotFoundError:
    with open ("guest.txt","w") as file:
        file.write("Welcome Guest")
    with open ("guest.txt") as file:
        file.read("guest.txt")