n = int(input("Введите количество чисел: "))

total = 0
pozitive_count = 0

number = int(input("Введите число: "))
total += number

if number >0:
    pozitive_count += 1

maximum = number

for x in range(n - 1):
    number = int(input("Введите число: "))
    total += number

    if number > 0:
        pozitive_count += 1

    if number > maximum:
        maximum = number

print(f"Сумма: {total}")
print(f"Число положительных чисел: {pozitive_count}")
print(f"Максимум: {maximum}")