storage = int(input("Заполненность хранилища: "))

if storage < 0 or storage > 100:
    print("Ошибка диапазона")
elif storage < 50:
    print("Свободно")
elif storage < 90:
    print("Мало места")
else: print("Почти заполнено")