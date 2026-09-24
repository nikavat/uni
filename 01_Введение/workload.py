predmet = input("Предмет: ")
zanyatiya = int(input("Количество занятий по предмету за неделю: "))
prod = int(input("Продолжительность одного занятия в минутах: "))
predmet2 = input("Второй предмет: ")
zanyatiya2 = int(input("Количество занятий по предмету за неделю: "))
prod2 = int(input("Продолжительность одного занятия в минутах: "))
vremya = int(input("Доступное время на неделю в часах: "))

predmet_vremya = zanyatiya * prod
predmet2_vremya = zanyatiya2 * prod2
obshie_min = predmet_vremya + predmet2_vremya
obshie_hours = obshie_min / 60
svobod_vremya = ((vremya * 60) - obshie_min) / 60
four_vremya = obshie_hours * 4

print(" ")
print("Учебная нагрузка")
print(f"Нагрузка по предмету {predmet}: {predmet_vremya} минут")
print(f"Нагрузка по предмету {predmet2}: {predmet2_vremya} минут")
print(f"Общая нагрузка: {obshie_min} минут, или же {obshie_hours:.2f} часов")
print(f"Остаток свободного времени: {svobod_vremya:.2f} часов")
print(f"Нагрузка за четыре одинаковые недели: {four_vremya:.2f} часов")