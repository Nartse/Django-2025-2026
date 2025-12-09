try:
    with open ("config.txt") as file:
        content=file.read("config.txt")
        file.read("Welcome, "+ content)
except Exception:
    with open ("guest.txt","w") as file:
        file.write("Guest")