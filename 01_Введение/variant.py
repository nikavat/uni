order = input("Название заказа: ")
name = input("Ваше имя: ")

order_name = input("Название первой позиции: ")
order_quantity = int(input("Количество: "))
order_price = float(input("Цена единицы в рублях: "))

order_name2 = input("Название второй позиции: ")
order_quantity2 = int(input("Количество: "))
order_price2 = float(input("Цена единицы в рублях: "))

delivery = float(input("Стоимость доставки: "))
amount_paid = float(input("Внесённая сумма: "))

cost = order_quantity * order_price
cost2 = order_quantity2 * order_price2

total_cost = cost + cost2
total_cost_with_delivery = total_cost + delivery
total_quantity = order_quantity + order_quantity2
change = amount_paid - total_cost_with_delivery

print("Название заказа: ", order)
print("Имя заказчика: ", name)

print("Название позиции | Кол-во | Цена единицы | Стоимость товаров")
print(f"{order_name} | {order_quantity} | {order_price:.2f} | {cost:.2f}")
print(f"{order_name2} | {order_quantity2} | {order_price2:.2f} | {cost2:.2f}")

print("Все итоги")
print(f"Стоимость товаров без доставки: {total_cost:.2f} руб.")
print(f"Стоимость доставки: {delivery:.2f} руб.")
print(f"Стоимость товаров с доставкой: {total_cost_with_delivery:.2f} руб.")
print(f"Общее количество единиц: {total_quantity}")
print(f"Внесенная сумма: {amount_paid:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")