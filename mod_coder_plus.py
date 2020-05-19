import random


def de_en_code(text):
    code = ''
    key = ''
    for index in hash_key:
        key = key + str(ord(index))
    for Ord in range(0, len(text)):
        if ord(text[Ord]) < 1424:
            code = code + chr((ord(text[Ord]) + ((-1) ** (Ord + Q)) * (s * Ord + int(key))) % 1424)
        else:
            return print('Присутствуют недопустимые символы! Один из таких:', text[Ord])
    with open(Directory, 'w+', encoding='utf-8') as txt:
        txt.write(code)
    if Q == 0:
        return print('Текст зашифрован! Основной ключ шифрования:', hash_key, ' Малый ключ шифрования:', s)
    if Q == 1:
        return print('Текст расшифрован!')


Directory = str(input('Укажите полный путь к текстовому файлу: '))
TxtFile = open(Directory, 'r', encoding='utf-8')
Q = int(input('Зашифровать (кнопка 0) | Расшифровать (кнопка 1): '))
if Q == 0:
    hash_key = str(input('Введите основной ключ шифрования, состоящий из любых символов '
                         '(малый ключ сгенерируется автоматически): '))
    s = random.randint(1, 99)
    de_en_code(TxtFile.read())
if Q == 1:
    hash_key = str(input('Введите основной ключ шифрования (состоит из рандомных символов): '))
    s = int(input('Введите малый ключ шифрования (это целое положительное число): '))
    de_en_code(TxtFile.read())
