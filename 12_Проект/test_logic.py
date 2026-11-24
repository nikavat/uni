from logic import*

def test_empty():
    records = []

    validate_records(records)

    assert statistics(records) == {
        "total": 0,
        "completed": 0,
        "unfinished": 0,
        "total_amount": 0,
        "categories": {}
    }

    assert find_records(records, "Пси") == []
    assert set_completed(records, 1, True) == False
    assert delete_record(records, 1) == False
# Проверяем, что пустой список считается корректным, статистика возвращает нули, а поиск, изменение статуса и удаление работают без ошибок.

def test_add():
    records = []

    add_record(records, "  Пси  ", "  Триллер  ", 320)
    add_record(records, "Пси", "Триллер", 320)

    assert len(records) == 2
    assert records[0]["id"] == 1
    assert records[1]["id"] == 2
    assert records[0]["title"] == "Пси"
    assert records[0]["category"] == "Триллер"
    assert records[0]["completed"] == False
# Здесь проверяем, что одинаковые названия разрешены, ID различаются, пробелы удаляются, а начальный статус равен False.

def test_find():
    records = []

    add_record(records, "Тени Сентфора", "Детектив", 250)

    assert find_records(records, "СЕНТ") == [records[0]]
    assert find_records(records, "  тени  ") == [records[0]]
    assert find_records(records, "Пси") == []

    try:
        find_records(records, "   ")
    except ValueError:
        pass
    else:
        assert False
# Пытаемся выполнить поиск с пустым запросом, получили ожидаемую ошибку, ничего не делаем, проверка успешна, если ошибки не возникло, тест провален.

def test_completed():
    records = []

    add_record(records, "Пси", "Триллер", 320)

    assert set_completed(records, 1, True) == True
    assert records[0]["completed"] == True

    assert set_completed(records, 99, False) == False
    assert records[0]["completed"] == True

    assert set_completed(records, 1, False) == True
    assert records[0]["completed"] == False
# Проверяем изменение статуса в обе стороны и убеждаемся, что при неизвестном ID данные не меняются.

def test_delete():
    records = []

    add_record(records, "Пси", "Триллер", 320)
    add_record(records, "Тени Сентфора", "Детектив", 250)

    assert delete_record(records, 99) == False
    assert len(records) == 2

    assert delete_record(records, 1) == True
    assert len(records) == 1
    assert records[0]["id"] == 2

    add_record(records, "Водяная лилия", "Триллер", 400)

    assert records[1]["id"] == 3
# Проверяем удаление, после удаления первой книги ID второй остаётся равным 2, а новая книга получает ID 3.

def test_statistics():
    records = []

    add_record(records, "Пси", "Триллер", 320)
    add_record(records, "Тени Сентфора", "Детектив", 250)
    add_record(records, "Водяная лилия", "Триллер", 400)

    set_completed(records, 1, True)

    assert statistics(records) == {
        "total": 3,
        "completed": 1,
        "unfinished": 2,
        "total_amount": 970,
        "categories": {
            "Детектив": 250,
            "Триллер": 720
        }
    }
# Проверяем статистику.

def check_invalid(records):
    try:
        validate_records(records)
    except ValueError:
        pass
    else:
        assert False
# Проверяем некорректные данные.

def test_validation():
    record = {
        "id": 1,
        "title": "Пси",
        "category": "Триллер",
        "amount": 320,
        "completed": False
    }

    validate_records([record])

    check_invalid({})
    check_invalid([123])
    check_invalid([record, record])

    check_invalid([dict(record, id=True)])
    check_invalid([dict(record, id=0)])
    check_invalid([dict(record, title="   ")])
    check_invalid([dict(record, title=123)])
    check_invalid([dict(record, category="")])
    check_invalid([dict(record, category=123)])
    check_invalid([dict(record, amount=-1)])
    # dict(record, amount=-1) - это удобный способ создать копию словаря, заменив значение одного ключа
    check_invalid([dict(record, amount=True)])
    check_invalid([dict(record, amount="320")])
    check_invalid([dict(record, amount=3.5)])
    check_invalid([dict(record, completed=1)])

    validate_records([dict(record, amount=0)])

    incomplete = record.copy()
    incomplete.pop("title")
    check_invalid([incomplete])

if __name__ == "__main__":
    test_empty()
    test_add()
    test_find()
    test_completed()
    test_delete()
    test_statistics()
    test_validation()

    print("Все тесты успешно пройдены")