total = int(input("Количество книг: "))
capacity = int(input("Вместимость коробок: "))

units = total // capacity
remainder = total % capacity
minimum = (total + capacity - 1) // capacity

print(f"Количество полностью заполненных коробок: {units} шт.")
print(f"Остаток книг: {remainder} шт.")
print(f"Минимальное число коробок для размещения всех книг: {minimum} шт.")