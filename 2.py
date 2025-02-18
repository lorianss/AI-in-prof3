def flood_fill(matrix, x, y, new_letter):
    # Получаем старую букву в точке (x, y)
    old_letter = matrix[x][y]

    # Если старая буква равна новой, ничего делать не нужно
    if old_letter == new_letter:
        return matrix

    # Рекурсивная функция для заливки
    def fill(x, y):
        # Проверяем границы матрицы
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return

        # Если текущая буква не равна старой, выходим
        if matrix[x][y] != old_letter:
            return

        # Заменяем текущую букву на новую
        matrix[x][y] = new_letter

        # Рекурсивно вызываем функцию для соседних ячеек
        fill(x + 1, y)  # Вниз
        fill(x - 1, y)  # Вверх
        fill(x, y + 1)  # Вправо
        fill(x, y - 1)  # Влево

    # Запускаем заливку
    fill(x, y)
    return matrix


# Создаем матрицу размером 7x7 с буквами
import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
matrix = [[random.choice(letters) for _ in range(7)] for _ in range(7)]

# Вывод исходной матрицы
print("Исходная матрица:")
for row in matrix:
    print(' '.join(row))

# Начальная точка и новая буква
x, y = 3, 3  # Начальная точка
new_letter = 'X'  # Новая буква

# Выполняем заливку
result = flood_fill(matrix, x, y, new_letter)

# Вывод результата
print("\nМатрица после заливки:")
for row in result:
    print(' '.join(row))