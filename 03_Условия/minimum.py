first = int(input("Первое число: "))
second = int(input("Второе число: "))
third = int(input("Третье число: "))

if second >= first and third >= first:
    minimum = first
elif first >= second and third >= second:
    minimum = second
else: minimum = third

print(f"Минимальное число: {minimum}")