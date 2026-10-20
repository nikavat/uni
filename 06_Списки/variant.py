text = input("Введите числа через пробел: ")
numbers = [int(part) for part in text.split()]
negative = []
for number in numbers:
    if number < 0:
        negative.append(number)
sorted_numbers = sorted(negative)

print(f"Исходный список: {numbers}")
print(f"Количество: {len(numbers)}")
print(f"Сумма: {sum(numbers)}")
print(f"Новая отсортированная копия: {sorted_numbers}")