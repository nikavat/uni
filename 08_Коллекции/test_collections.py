from collections_lab import *

assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}

first = ["python", "sql", "python"]
second = ["sql", "git"]
assert common_topics(first, second) == ["sql"]
assert all_topics(first, second) == ["git", "python", "sql"]
assert common_topics([], second) == []
assert all_topics([], second) == ["git", "sql"]

record, pair = record_example()
assert record == {
    "title": "Python",
    "hours": 7,
    "completed": False
}
assert pair == ("Python", 7)

books = [
    {"title": "Python для начинающих", "category": "программирование", "amount": 7},
    {"title": "Алгоритмы", "category": "программирование", "amount": 4},
    {"title": "Алгебра", "category": "математика", "amount": 3},
    {"title": "История России", "category": "история", "amount": 5},
    {"title": "Геометрия", "category": "математика", "amount": 2}
]
totals = totals_by_category(books)
print("Количество книг по категориям:")
for category in sorted(totals):
    print(f"{category}: {totals[category]}")

category = input("Введите категорию: ")
result = titles_in_category(books, category)
print("Найденные книги: ", result)

assert totals_by_category(books) == {
    "программирование": 11,
    "математика": 5,
    "история": 5
}
assert titles_in_category(books, "кулинария") == []
assert totals_by_category([]) == {}
assert titles_in_category([], "математика") == []
original = [record.copy() for record in books]
totals_by_category(books)
titles_in_category(books, "программирование")
assert books == original

print("Все проверки пройдены")