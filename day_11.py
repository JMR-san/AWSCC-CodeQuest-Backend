with open('name.txt', 'a') as file:
    name = input("Enter your name: ")
    file.write(f"{name}\n")

with open ('name.txt', 'r') as file: 
    contents = file.readlines()
    contents.sort()
    for name in contents:
        print(f"{name.strip()}")