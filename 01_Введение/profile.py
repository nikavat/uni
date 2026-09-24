surname = input("Фамилия: ")
name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст: "))
future_age = age + 4
fav_subjects = input("Любимый предмет: ")
weekly_hours = float(input("Часов подготовки в неделю: "))
four_weekly_hours = weekly_hours * 4
daily_hours = weekly_hours/7
print("Учебная карточка")
print(f"Имя: {name}")
print(f"Фамилия: {surname}")
print(f"Возраст через четыре года: {future_age}")
print(f"За четыре недели: {four_weekly_hours} ч")
print(f"В среднем за день: {daily_hours:.2} ч")