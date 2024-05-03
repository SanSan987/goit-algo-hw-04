import timeit
import random

# Алгоритм вставка-сортування
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Алгоритм злиття-сортування
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])

        arr = []
        while left_half and right_half:
            if left_half[0] < right_half[0]:
                arr.append(left_half.pop(0))
            else:
                arr.append(right_half.pop(0))
        arr.extend(left_half or right_half)
    return arr

def measure_time(func):
    start_time = timeit.default_timer()
    func()
    return timeit.default_timer() - start_time

# Генеруємо рандомні набори (масиви)
sizes = [100, 500, 1000]
results = {}

for size in sizes:
    arr = [random.randint(0, 100000) for _ in range(size)]
    data_for_sort = arr[:] 
    data_for_insertion = arr[:]
    data_for_merge = arr[:]

    time_timsort = measure_time(lambda: data_for_sort.sort())
    time_insertion = measure_time(lambda: insertion_sort(data_for_insertion))
    time_merge = measure_time(lambda: merge_sort(data_for_merge))

    results[size] = {'Timsort': time_timsort, 'Вставка-сортування': time_insertion, 'Злиття-сортування': time_merge}

print(results)

# Час виконання на згенеровані рандомно 100: 500: 1000: елементів трьома алгоритмами:
# 100: {'Timsort': 7.6000578701496124e-06, 'Вставка-сортування': 0.00018370011821389198, 'Злиття-сортування': 0.00011539994738996029}, 
# 500: {'Timsort': 3.9599835872650146e-05, 'Вставка-сортування': 0.004973500035703182, 'Злиття-сортування': 0.0007128999568521976}, 
# 1000: {'Timsort': 8.819997310638428e-05, 'Вставка-сортування': 0.02483469992876053, 'Злиття-сортування': 0.0015382999554276466}}
"""Висновки: Timsort є найшвидшим алгоритмом сортування на всіх розмірах даних.
«Вставка» показує значне збільшення часу сортування зі збільшенням розміру даних. Це відповідає його теоретичній складності O(n^2), 
що робить його неефективним для великих даних, але прийнятним для малих наборів.
«Злиття» демонструє кращі результати, ніж «вставка», особливо при збільшенні обсягу даних. Його час виконання росте менш стрімко завдяки тому, 
що його складність складає O(n log n). Це робить «злиття» вигіднішим вибором (від "вставки") для більших наборів даних.
Timsort - ЧЕМПІОН ! """