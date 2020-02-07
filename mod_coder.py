def de_en_code(text):
    code = ''
    for Ord in range(0, len(text)):
        if ord(text[Ord]) < 1424:
            code = code + chr((ord(text[Ord]) + ((-1) ** (Ord + Q)) * ((Ord + 1) * 2)) % 1424)
        else:
            return print('Присутствуют недопустимые символы!')
    with open(Directory, 'w+', encoding='utf-8') as file:
        file.write(code)
    return print('Файл готов')


Directory = str(input('Укажите полный путь к текстовому файлу: '))
File = open(Directory, 'r', encoding='utf-8')
Q = int(input('Зашифровать (кнопка 0) | Расшифровать (кнопка 1): '))
de_en_code(File.read())
