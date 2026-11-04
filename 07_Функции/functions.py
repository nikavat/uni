def sum_digits(number):
    number = abs(number)
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def normalize_text(text):
    text = " ".join(text.lower().split())
    return text

def select_numbers(numbers, threshold):
    result = []
    for number in numbers:
        if number < threshold:
            result.append(number)
    return result