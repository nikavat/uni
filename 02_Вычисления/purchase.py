price = int(input("Цена одной тетради в целых рублях: "))
count = int(input("Количество тетрадей: "))
paid = int(input("Переданная сумма: "))

cost = price * count
change = paid - cost

print(f"Стоимость тетрадей {cost} руб., сдача {change} руб.")