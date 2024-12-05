import math

def task_variant_12(r):
    """Вычислить площади круга и прямоугольного треугольника с радиусом r."""
    try:
        # Проверяем, что радиус положительный
        if r <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        
        # Площадь круга
        area_circle = math.pi * r**2
        
        # Площадь прямоугольного треугольника
        area_triangle = (r * r) / 2
        
        print(f"Площадь круга с радиусом {r} равна: {area_circle:.2f}")
        print(f"Площадь прямоугольного треугольника с катетами {r} равна: {area_triangle:.2f}")
        
        return area_circle, area_triangle
    
    except ValueError as ve:
        print(f"Ошибка: {ve}")
        return None

# Пример вызова функции
r = float(input("Введите радиус r: "))
task_variant_12(r)
