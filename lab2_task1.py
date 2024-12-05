# module m.py
def task_if19():
    """If19. Дано чотири цілих числа, одне з яких відмінно від трьох інших, рівних між собою.
    Визначити порядковий номер числа, відмінного від інших."""
    try:
        # Вводим четыре целых числа
        nums = [int(input(f"Число {i+1}: ")) for i in range(4)]

        # Определяем порядковый номер отличного числа
        if nums[0] == nums[1] == nums[2]:
            unique_num_index = 3
        elif nums[0] == nums[1] == nums[3]:
            unique_num_index = 2
        elif nums[0] == nums[2] == nums[3]:
            unique_num_index = 1
        else:
            unique_num_index = 0

        print("Порядковый номер отличного числа:", unique_num_index + 1)
    except ValueError:
        print("Ожидается целое число!")

# Вызываем функцию для проверки
task_if19()
