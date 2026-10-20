text = input("Введите числа через пробел: ")
numbers = [int(part) for part in text.split()]
if len(numbers) == 0:
    print("Нет данных")
else:
    maximum = max(numbers)
    positions = []
    for index, number in enumerate(numbers):
        if number == maximum:
            positions.append(index)
    print(f"Максимум: {maximum}")
    print(f"Индексы максимума: {positions}")