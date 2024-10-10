import timeit
from task03lib import kmp_search, boyer_moore_search,rabin_karp_search

# Читаємо текст з файлів
dirfile1 = "article1.txt"
dirfile2 = "article2.txt"

with open(dirfile1, "r", encoding="windows-1251") as file1, open(dirfile2, "r", encoding="utf-8") as file2:
    article1 = file1.read()
    article2 = file2.read()

# Підрядки для пошуку
existing_substring_article1 = "найбільші за номіналом монети"  # Існуючий підрядок статті 1
existing_substring_article2 = "Бінарні діаграми рішень"  # Існуючий підрядок статті 2
non_existing_substring = "пайтон це мова програмування"  # Вигаданий підрядок

# Функція для вимірювання часу виконання алгоритму, з повтеренням для більшої точності
def measure_time(search_func, text, pattern):
    return timeit.timeit(lambda: search_func(text, pattern), number=100)  

# Словник для збереження результатів часу
results = {}

# Дані для тестування
tests = [
    {"name": "Стаття 1 - Існуючий рядок", "article": article1, "substring": existing_substring_article1},
    {"name": "Стаття 1 - Неіснуючий рядок", "article": article1, "substring": non_existing_substring},
    {"name": "Стаття 2 - Існуючий рядок", "article": article2, "substring": existing_substring_article2},
    {"name": "Стаття 2 - Неіснуючий рядок", "article": article2, "substring": non_existing_substring}
]

# Алгоритми для порівняння
algorithms = {
    "КМП": kmp_search,
    "Боєра-Мура": boyer_moore_search,
    "Рабіна-Карпа": rabin_karp_search
}

# Порівняння для кожного тесту
for test in tests:
    print(f"\n{test['name']}:")
    
    min_time = float('inf')
    fastest_algorithm = None
    
    # Виконуємо кожен алгоритм
    for algo_name, algo_func in algorithms.items():
        time_taken = measure_time(algo_func, test['article'], test['substring'])
        print(f"{algo_name}: {time_taken:.6f} секунд")
        
        # Записуємо результат у словник
        results[(test['name'], algo_name)] = time_taken
        
        # Знаходимо найшвидший алгоритм
        if time_taken < min_time:
            min_time = time_taken
            fastest_algorithm = algo_name
    
    # Виводимо назву найшвидшого алгоритму для цього тесту
    print(f"Найшвидший алгоритм: {fastest_algorithm}\n")
