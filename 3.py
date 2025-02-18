def longest_alphabetical_path(matrix, start_char):
    # Получаем размер матрицы
    rows, cols = len(matrix), len(matrix[0])

    # Проверяем, находится ли координата внутри матрицы
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # Функция для получения следующего символа в алфавите
    def next_char(c):
        if c == 'Z':
            return None  # После 'Z' нет следующего символа
        return chr(ord(c) + 1)

    # Рекурсивная функция для поиска пути
    def dfs(x, y, current_char, memo):
        # Если результат уже вычислен, используем его
        if memo[x][y] != -1:
            return memo[x][y]

        max_length = 1  # Минимальная длина пути — это сам символ

        # Проверяем все восемь направлений
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):  # Проверяем, что новая координата внутри матрицы
                if matrix[nx][ny] == next_char(current_char):  # Проверяем последовательность
                    length = 1 + dfs(nx, ny, matrix[nx][ny], memo)  # Продолжаем путь
                    max_length = max(max_length, length)

        # Сохраняем результат в мемоизацию
        memo[x][y] = max_length
        return max_length

    # Ищем все возможные стартовые точки для заданного символа
    max_path_length = 0
    memo = [[-1 for _ in range(cols)] for _ in range(rows)]  # Мемоизация

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == start_char:
                path_length = dfs(i, j, start_char, memo)
                max_path_length = max(max_path_length, path_length)

    return max_path_length


# Пример использования
matrix = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    ['P', 'Q', 'R', 'S', 'T'],
    ['U', 'V', 'W', 'X', 'Y']
]

start_char = 'A'  # Начинаем с символа 'A'

result = longest_alphabetical_path(matrix, start_char)
print(f"Длина самого длинного пути: {result}")