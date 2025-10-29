import timeit
import time
import matplotlib.pyplot as plt

def memoize(func):
    cache = {}
    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return memoized_func

# рекурсивное вычисление факториала
def fact_recursive(n):
    if n <= 1:
        return 1
    else:
        return n * fact_recursive(n - 1)

# нерекурсивное вычисление факториала
def fact_iterative(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

# Значения для тестирования
values = list(range(10, 101, 25))

print("=== ВЫЧИСЛЕНИЕ ФАКТОРИАЛОВ ОТ 10 ДО 100 С ШАГОМ 25 ===\n")

# ============================================================
# ЧИСТЫЙ БЕНЧМАРК ОДНОГО ВЫЗОВА
# ============================================================

print("=== ЧИСТЫЙ БЕНЧМАРК ОДНОГО ВЫЗОВА ===")
single_call_times = {
    'recursive': [],
    'iterative': [],
    'recursive_memo': [],
    'iterative_memo': []
}

for n in values:
    print(f"\n--- n = {n} ---")
    
    # Рекурсивный метод (один вызов)
    start_time = time.perf_counter()
    result_rec = fact_recursive(n)
    end_time = time.perf_counter()
    time_rec = end_time - start_time
    single_call_times['recursive'].append(time_rec)
    
    # Итеративный метод (один вызов)
    start_time = time.perf_counter()
    result_iter = fact_iterative(n)
    end_time = time.perf_counter()
    time_iter = end_time - start_time
    single_call_times['iterative'].append(time_iter)
    
    # Рекурсивный с мемоизацией (один вызов)
    fact_rec_memo = memoize(fact_recursive)
    start_time = time.perf_counter()
    result_rec_memo = fact_rec_memo(n)
    end_time = time.perf_counter()
    time_rec_memo = end_time - start_time
    single_call_times['recursive_memo'].append(time_rec_memo)
    
    # Итеративный с мемоизацией (один вызов)
    fact_iter_memo = memoize(fact_iterative)
    start_time = time.perf_counter()
    result_iter_memo = fact_iter_memo(n)
    end_time = time.perf_counter()
    time_iter_memo = end_time - start_time
    single_call_times['iterative_memo'].append(time_iter_memo)
    
    print(f"Рекурсивный:          {time_rec:.8f} сек")
    print(f"Итеративный:          {time_iter:.8f} сек")
    print(f"Рекурсивный (мемо):   {time_rec_memo:.8f} сек")
    print(f"Итеративный (мемo):   {time_iter_memo:.8f} сек")

# ============================================================
# СТАНДАРТНЫЙ БЕНЧМАРК (100 ВЫЗОВОВ)
# ============================================================

print("\n\n=== СТАНДАРТНЫЙ БЕНЧМАРК (100 ВЫЗОВОВ) ===")

print("\n=== БЕЗ МЕМОИЗАЦИИ ===")
for n in values:
    # Рекурсивный метод
    result_recursive = fact_recursive(n)
    time_recursive = timeit.timeit(lambda: fact_recursive(n), number=100, globals=globals())
    
    # Итеративный метод
    result_iterative = fact_iterative(n)
    time_iterative = timeit.timeit(lambda: fact_iterative(n), number=100, globals=globals())
    
    print(f"n = {n}:")
    print(f"  Рекурсивный: результат = {result_recursive}, время = {time_recursive:.6f} сек")
    print(f"  Итеративный: результат = {result_iterative}, время = {time_iterative:.6f} сек")
    print()

print("\n=== С МЕМОИЗАЦИЕЙ ===")
time_recursive_100 = []
time_iterative_100 = []
time_recursive_memo_100 = []
time_iterative_memo_100 = []

for n in values:
    # Создаем новые мемоизированные функции для каждого n
    fact_recursive_memo = memoize(fact_recursive)
    fact_iterative_memo = memoize(fact_iterative)
    
    # Рекурсивный метод с мемоизацией
    result_recursive_memo = fact_recursive_memo(n)
    time_rec_memo = timeit.timeit(lambda: fact_recursive_memo(n), number=100, globals=globals())
    time_recursive_memo_100.append(time_rec_memo)
    
    # Итеративный метод с мемоизацией
    result_iterative_memo = fact_iterative_memo(n)
    time_iter_memo = timeit.timeit(lambda: fact_iterative_memo(n), number=100, globals=globals())
    time_iterative_memo_100.append(time_iter_memo)
    
    # Без мемоизации для сравнения
    time_rec = timeit.timeit(lambda: fact_recursive(n), number=100, globals=globals())
    time_iter = timeit.timeit(lambda: fact_iterative(n), number=100, globals=globals())
    time_recursive_100.append(time_rec)
    time_iterative_100.append(time_iter)
    
    print(f"n = {n}:")
    print(f"  Рекурсивный (мемо): результат = {result_recursive_memo}, время = {time_rec_memo:.6f} сек")
    print(f"  Итеративный (мемo): результат = {result_iterative_memo}, время = {time_iter_memo:.6f} сек")
    print()

# ============================================================
# ПОСТРОЕНИЕ ГРАФИКОВ
# ============================================================

# График 1: Чистый бенчмарк одного вызова
plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
plt.plot(values, single_call_times['recursive'], 'ro-', label='Рекурсивный', linewidth=2, markersize=8)
plt.plot(values, single_call_times['iterative'], 'bo-', label='Итеративный', linewidth=2, markersize=8)
plt.plot(values, single_call_times['recursive_memo'], 'go-', label='Рекурсивный (мемо)', linewidth=2, markersize=8)
plt.plot(values, single_call_times['iterative_memo'], 'mo-', label='Итеративный (мемо)', linewidth=2, markersize=8)
plt.title('ЧИСТЫЙ БЕНЧМАРК: время одного вызова', fontsize=12, fontweight='bold')
plt.xlabel('n (значение факториала)')
plt.ylabel('Время выполнения (секунды)')
plt.legend()
plt.grid(True, alpha=0.3)

# Добавляем аннотации для чистого бенчмарка
for i, n in enumerate(values):
    plt.annotate(f'{single_call_times["recursive"][i]:.6f}', 
                (n, single_call_times['recursive'][i]), 
                textcoords="offset points", xytext=(0,10), 
                ha='center', fontsize=7, color='red')
    plt.annotate(f'{single_call_times["iterative"][i]:.6f}', 
                (n, single_call_times['iterative'][i]), 
                textcoords="offset points", xytext=(0,-15), 
                ha='center', fontsize=7, color='blue')

# График 2: Стандартный бенчмарк (100 вызовов)
plt.subplot(1, 2, 2)
plt.plot(values, time_recursive_100, 'ro-', label='Рекурсивный', linewidth=2, markersize=8)
plt.plot(values, time_iterative_100, 'bo-', label='Итеративный', linewidth=2, markersize=8)
plt.plot(values, time_recursive_memo_100, 'go-', label='Рекурсивный (мемо)', linewidth=2, markersize=8)
plt.plot(values, time_iterative_memo_100, 'mo-', label='Итеративный (мемо)', linewidth=1, markersize=4)
plt.title('СТАНДАРТНЫЙ БЕНЧМАРК: 100 вызовов', fontsize=12, fontweight='bold')
plt.xlabel('n (значение факториала)')
plt.ylabel('Время выполнения (секунды)')
plt.legend()
plt.grid(True, alpha=0.3)

# Добавляем аннотации для стандартного бенчмарка
for i, n in enumerate(values):
    plt.annotate(f'{time_recursive_100[i]:.6f}', 
                (n, time_recursive_100[i]), 
                textcoords="offset points", xytext=(0,10), 
                ha='center', fontsize=7, color='red')
    plt.annotate(f'{time_iterative_100[i]:.6f}', 
                (n, time_iterative_100[i]), 
                textcoords="offset points", xytext=(0,-15), 
                ha='center', fontsize=7, color='blue')

plt.tight_layout()
plt.show()

# ============================================================
# СРАВНИТЕЛЬНАЯ ТАБЛИЦА
# ============================================================

print("\n=== СРАВНИТЕЛЬНАЯ ТАБЛИЦА ===")
print(f"{'n':<4} {'1 вызов рекурс':<14} {'100 вызовов рекурс':<18} {'1 вызов итер':<14} {'100 вызовов итер':<18}")
print("-" * 80)

for i, n in enumerate(values):
    print(f"{n:<4} {single_call_times['recursive'][i]:<14.8f} {time_recursive_100[i]:<18.8f} {single_call_times['iterative'][i]:<14.8f} {time_iterative_100[i]:<18.8f}")