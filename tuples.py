contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

name = input("Enter the name: ")

found = False
for contact in contacts:
    if contact[0] == name:
        age = contact[1]
        print(f"{name} is {age}")
        found = True
        break

if not found:
    print("Not Found")