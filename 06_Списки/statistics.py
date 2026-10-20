text = input("Целые числа через пробел: ")
if text.strip() == "":
    print("Нет данных")
else:
    numbers = [int(part) for part in text.split()]
    numbers.sort()
    print(f"Количество: {len(numbers)}")
    print(f"Сумма: {sum(numbers)}")
    print(f"Минимум: {numbers[0]}")
    print(f"Максимум: {numbers[-1]}")
    print(f"Среднее: {(sum(numbers) / len(numbers)):.2f}")