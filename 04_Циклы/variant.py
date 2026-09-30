n = int(input("Введите количество чисел: "))

count = 0
total = 0

for x in range(n):
    number = int(input("Введите число: "))
    if number < 0:
        count +=1
        total += number
print(f"Количество: {count}")
print(f"Сумма: {total}")