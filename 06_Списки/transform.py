numbers = []
for part in input("Введите числа через пробел: ").split():
    numbers.append(int(part))

transform = []
for number in numbers:
    if number < 0:
        transform.append(abs(number))
    else:
        transform.append(number)

print(f"Исходный список: {numbers}")
print(f"Новый список: {transform}")