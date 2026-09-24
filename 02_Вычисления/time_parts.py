total_seconds = int(input("Количество секунд: "))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = (total_seconds % 3600) % 60

print(f"{total_seconds} секунд - это {hours} ч. {minutes} мин. {seconds} с.")