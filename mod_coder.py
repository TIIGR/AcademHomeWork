def de_en_code(text):
    code = ''
    for Ord in range(0, len(text)):
        if ord(text[Ord]) < 1424:
            code = code + chr((ord(text[Ord]) + ((-1) ** (Ord + Q)) * ((Ord + 1) * 2)) % 1424)
        else:
            exit('Присутствуют недопустимые символы!')
    return code


Text = str(input('Введите текст: '))
Q = int(input('Зашифровать (введите четное число) | Расшифровать (введите нечетное число): '))
print(de_en_code(Text))  # Если эту функцию применять 1424 раза, получится исходный текст.
