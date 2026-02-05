

if __name__ == "__main__":
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print("Fruit:", fruit)

    for i in range(1, 6):
        print("i:", i)

    word = "python"
    for ch in word:
        print(ch)

    user = {"name": "Жасаби", "age": 18, "city": "Almaty"}
    for key in user:
        print(key, "->", user[key])

    for i in range(1, 4):
        for j in range(1, 3):
            print(f"({i},{j})")
