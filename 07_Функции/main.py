from functions import *
def main():
    number = int(input("Введите целое число: "))
    print("Сумма цифр: ", sum_digits(number))

    numbers = list(map(int, input("Введите числа через пробел: ").split()))
    result = average(numbers)
    if result == None:
        print("Нет данных")
    else: print("Среднее арифметическое: ", result)

    text = input("Введите текст: ")
    print("Нормализованный текст: ", normalize_text(text))

    threshold_numbers = list(map(int, input("Введите числа для отбора через пробел: ").split()))
    threshold = int(input("Введите порог: "))
    selected = select_numbers(threshold_numbers, threshold)
    print("Выбранные числа: ", selected)

if __name__ == '__main__':
    main()