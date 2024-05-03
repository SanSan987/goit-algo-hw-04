# Порівння швидкості двох вбудованих в Python функцій sort(), sorted()
import timeit
import random

def generate_data(size):
    return [random.randint(0, 100000) for _ in range(size)]

def measure_time(func):
    start_time = timeit.default_timer()
    func()
    return timeit.default_timer() - start_time

sizes = [100, 500, 1000]
results = {}

for size in sizes:
    data = generate_data(size)
    data_copy = data[:]
    
    # Вимірювання часу для sorted()
    time_sorted = measure_time(lambda: sorted(data))
    
    # Вимірювання часу для sort()
    time_sort = measure_time(lambda: data_copy.sort())

    results[size] = (time_sorted, time_sort)

print(results)

# Час виконання на згенеровані рандомно 100: 500: 1000: елементів (перше - 'sorted', друге - 'sort'):
# {100: (8.899951353669167e-06, 5.700159817934036e-06), 500: (4.449998959898949e-05, 3.50000336766243e-05), 1000: (8.829985745251179e-05, 8.649984374642372e-05)}
"""Висновок: Вбудована функція ‘sort’ швидша для малого масиву (100 елементів), але різниця у швидкості зменшується із збільшенням розміру масиву. 
Це може свідчити про те, що функція ‘sort’ ефективніша для менших даних, але обидві функції демонструють схожу ефективність при збільшенні розміру масиву. """