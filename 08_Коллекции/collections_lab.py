def word_counts(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        word = word.strip(".,!?;:")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts

def sorted_word_counts(counts):
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")
    return counts

def common_topics(first, second):
    return sorted(set(first) & set(second))

def all_topics(first, second):
    return sorted(set(first) | set(second))

def record_example():
    record = {
        "title": "Python",
        "hours": 3
    }
    record["hours"] = 7
    record["completed"] = False

    pair = (record["title"], record["hours"])
    title = pair[0]
    hours = pair[1]
    print(record)
    print(f"Пара: {title}, {hours}")
    return record, pair


def totals_by_category(records):
    totals = {}
    for record in records:
        category = record["category"]
        amount = record["amount"]
        totals[category] = totals.get(category, 0) + amount
    return totals

def titles_in_category(records, category):
    titles = []
    for record in records:
        if record["category"] == category:
            titles.append(record["title"])
    return titles

if __name__ == "__main__":
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