text = input("Введите текст: ")

replace = text.lower().replace(" ", "")

if replace == "":
    print("Нет текста")
elif replace == replace[::-1]:
    print("Палиндром")
else: print("Не палиндром")