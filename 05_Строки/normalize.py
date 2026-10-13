text = input("Введите текст: ")
words = text.split()
normalized = ' '.join(words)

old_length = len(text)

print(f"Исходная длина: {old_length}")
print(f"Новая длина: {len(normalized)}")
print(f"Нормализованный текст: {normalized}")
print(f"Количество слов: {len(normalized.split())}")