products = [
    {"назва": "Молоко", "ціна": 20, "кількість": 10},
    {"назва": "Хліб", "ціна": 10, "кількість": 20},
    {"назва": "Яблука", "ціна": 5, "кількість": 15}
]
users = []
while True:
    print("Меню:")
    print("1. Зареєструватись")
    print("2. Увійти")
    print("3. Купити товар")
    print("4. Показати товар")
    print("5. Змінити товар (тільки для адміністратора)")
    print("6. Вийти")
    choice = input("Виберіть пункт меню: ")
    if choice == "1":
        username = input("Введіть логін: ")
        password = input("Введіть пароль: ")
        users.append({"логін": username, "пароль": password})
        print("Реєстрація пройшла успішно!")
    elif choice == "2":
        username = input("Введіть логін: ")
        password = input("Введіть пароль: ")
        if {"логін": username, "пароль": password} in users:
            print("Успішний вхід!")
        else:
            print("Невірний логін або пароль.")
    elif choice == "3":
        if not users:
            print("Спочатку потрібно зареєструватись!")
            continue
        total_price = 0
        cart = []
        while True:
            product_name = input("Введіть назву товару: ")
            quantity = int(input("Введіть кількість товару: "))
            for product in products:
                if product["назва"] == product_name:
                    if product["кількість"] >= quantity:
                        total_price += product["ціна"] * quantity
                        cart.append({"назва": product_name, "кількість": quantity})
                        product["кількість"] -= quantity
                    else:
                        print("Недостатня кількість товару.")
                    break
            else:
                print("Товар не знайдено.")
            choice = input("Продовжити покупки? (так/ні): ")
            if choice.lower() == "ні":
                break
        print("Сума до оплати:", total_price)
    elif choice == "4":
        for product in products:
            print(f"Назва: {product['назва']}, Ціна: {product['ціна']}, Кількість: {product['кількість']}")
    elif choice == "5":
        admin_username = input("Введіть логін адміністратора: ")
        admin_password = input("Введіть пароль адміністратора: ")

        if {"логін": admin_username, "пароль": admin_password} in users and admin_username == "Admin" and admin_password == "Admin":
            product_name = input("Введіть назву товару, який хочете змінити: ")

            for product in products:
                if product["назва"] == product_name:
                    print("Що ви хочете змінити?")
                    print("1. Назву")
                    print("2. Ціну")
                    print("3. Кількість")
                    choice = input("Виберіть пункт меню: ")

                    if choice == "1":
                        new_name = input("Введіть нову назву: ")
                        product["назва"] = new_name
                        print("Назву змінено успішно!")
                    elif choice == "2":
                        new_price = float(input("Введіть нову ціну: "))
                        product["ціна"] = new_price
                        print("Ціну змінено успішно!")
                    elif choice == "3":
                        new_count = int(input("Введіть нову кількість: "))
                        product["кількість"] = new_count
                        print("Кількість змінено успішно!")
                    else:
                        print("Невірний вибір.")

                    break
            else:
                print("Товар не знайдено.")
        else:
            print("Невірний логін або пароль адміністратора.")

    elif choice == "6":
        print("До побачення!")
        break

    else:
        print("Невірний вибір.")





