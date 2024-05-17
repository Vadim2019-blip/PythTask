def normalize_path(path: str) -> str:
    # Проверяем, если путь пустой, возвращаем текущую директорию
    if path == '':
        return '.'

    # Проверяем, является ли путь абсолютным
    root = path[0] == "/"

    # Разделяем путь на папки
    directories = [directory for directory in path.split('/') if directory and directory != '.']

    # Инициализируем стек
    stack = []

    # Обрабатываем каждую часть пути
    for directory in directories:
        if directory == "..":
            if stack and stack[-1] != "..":
                stack.pop()
            elif not root:
                stack.append("..")
        else:
            stack.append(directory)

    normalized_path = '/' * root + '/'.join(stack)

    return normalized_path if normalized_path else "."