import math

def compute_series(n_max=100):
    total = 0
    for n in range(1, n_max + 1):
        term = (math.exp(2 * n + 1) + n) / math.sqrt(math.factorial(n))
        total += term
    return total

# Пример использования:
n_max = int(input("Введите максимальное значение n для вычисления суммы: "))
result = compute_series(n_max)
print(f"Результат суммы для n от 1 до {n_max}: {result:.6f}")
