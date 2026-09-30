year = int(input("Введите год: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Этот год високосный")
elif 1 <= year <= 9999:
    print("Этот год не високосный")
else: print("Ошибка")