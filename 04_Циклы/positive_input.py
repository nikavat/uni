count = 0
number = int(input("Введите положительное число: "))

while number <= 0:
    count += 1
    number = int(input("Введите положительное число: "))

print(f"Квадрат числа: {number**2}")
print(f"Количество отклоненных попыток: {count}")