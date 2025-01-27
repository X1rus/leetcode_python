def sum_two_smallest_numbers(numbers):
    first_min = None  # Найменше число
    second_min = None  # Друге найменше число

    for num in numbers:
        if num > 0:  # Беремо лише позитивні числа
            if first_min is None or num < first_min:
                second_min = first_min  # Переміщаємо попереднє найменше в second_min
                first_min = num  # Оновлюємо найменше
            elif second_min is None or first_min < num < second_min:
                second_min = num  # Оновлюємо друге найменше

    return first_min+second_min

#def sum_two_smallest_numbers(numbers):
#    return sum(sorted(numbers)[:2])

print(sum_two_smallest_numbers([-5,8,12,18,22]))