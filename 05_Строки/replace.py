text = input("Введите текст: ")

count = text.count(":")
replace = text.replace(":","-")

print(f"Количество замен: {count}")
print(f"Новая строка: {replace}")