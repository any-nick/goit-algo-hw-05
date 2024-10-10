def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1  # Підраховуємо кількість ітерацій
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            upper_bound = arr[mid]  # Можливий кандидат на верхню межу
            high = mid - 1
        else:
            return (iterations, arr[mid])  # Якщо знайдений елемент

    # Якщо елемент не знайдений, повертаємо кількість ітерацій і найближчу верхню межу
    return (iterations, upper_bound)

# Тестуємо функцію:
arr = [1.1, 1.52, 3.48, 4.4, 6.26, 8.12, 10.9, 12.29, 15.5, 18.4, 22.3]
target = 9.12

result = binary_search(arr, target)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")
