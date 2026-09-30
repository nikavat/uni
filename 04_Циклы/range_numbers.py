a = int(input("Введите a: "))
b = int(input("Введите b: "))

if a < b:
    for numbers in range(a, b + 1):
        print(numbers)
elif a > b:
    for numbers in range(a, b - 1, -1):
        print(numbers)
else:
    print(a)