text = input("Введите текст: ")

words = text.split()
count = 0

for word in words:
    cleaned = word.strip(".,!?;:").lower()
    if cleaned == "":
        continue
    if cleaned.endswith("я"):
        count += 1
        print(cleaned)
if count == 0:
    print("Нет совпадений")

print(f"Общее количество: {count}")