def de_en_code(text):
    code = ''
    error = 'Присутствуют недопустимые символы: '
    for Ord in range(0, len(text)):
        if ord(text[Ord]) < 1424:
            code = code + chr((ord(text[Ord]) + ((-1) ** (Ord + Q)) * ((Ord + 1) * 2)) % 1424)
        else:
            error = error + text[Ord]
    if error == 'Присутствуют недопустимые символы: ':
        return code
    else:
        return error


Text = str(input('Введите текст: '))
Q = int(input('Зашифровать (введите четное число) | Расшифровать (введите нечетное число): '))
print(de_en_code(Text))  # Если эту функцию применять 1424 раза, получится исходный текст (N - нат. число)
