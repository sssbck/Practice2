

if __name__ == "__main__":
    number = 7

    if number % 2 == 0:
        print("even")
    else:
        print("odd")

    password = "1234"
    if password == "admin":
        print("Доступ разрешён")
    else:
        print("Неверный пароль")

    a = 10
    b = 20
    if a > b:
        print("a больше b")
    else:
        print("b больше или равно a")

    user_input = ""
    if user_input:
        print("Ввод:", user_input)
    else:
        print("Пустой ввод")
