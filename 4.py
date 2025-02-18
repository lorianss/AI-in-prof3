def load_russian_dictionary():
    return set([
        "КАТЕ", "ЛО", "ЛЬ", "СЕН", "СЕНО", "КАТ",
        "ДОМ", "СТОЛ", "КНИГА", "ГОРКА", "ЛЕС"
    ])

# Функция поиска осмысленных слов
def find_meaningful_words(matrix, dictionary):
    # Получаем размер матрицы
    rows, cols = len(matrix), len(matrix[0])

    # Проверяем, находится ли координата внутри матрицы
    def is_valid(x, y, visited):
        return 0 <= x < rows and 0 <= y < cols and not visited[x][y]

    # Рекурсивная функция для поиска слов
    def dfs(x, y, path, visited, words):
        # Добавляем текущую ячейку в путь
        path.append(matrix[x][y])
        current_word = ''.join(path)

        # Если текущее слово есть в словаре, добавляем его в результат
        if current_word in dictionary:
            words.add(current_word)

        # Проверяем все восемь направлений
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited):  # Если новая координата допустима
                visited[nx][ny] = True
                dfs(nx, ny, path, visited, words)
                visited[nx][ny] = False  # Снимаем метку посещения

        # Убираем текущую ячейку из пути (backtracking)
        path.pop()

    # Множество для хранения всех найденных слов
    all_words = set()

    # Перебираем каждую ячейку как начальную точку
    for i in range(rows):
        for j in range(cols):
            visited = [[False for _ in range(cols)] for _ in range(rows)]  # Матрица посещенных ячеек
            visited[i][j] = True
            dfs(i, j, [], visited, all_words)

    return list(all_words)


# Пример использования
matrix = [
    ['К', 'А', 'Т'],
    ['О', 'Л', 'Ь'],
    ['С', 'Е', 'Н']
]

# Загружаем словарь русских слов (можно заменить на реальный файл)
dictionary = load_russian_dictionary()

result = find_meaningful_words(matrix, dictionary)
print("Найденные осмысленные слова:")
print(result)