import random


def de_en_code(text):
    code = ''
    for Ord in range(0, len(text)):
        if ord(text[Ord]) < 1424:
            code = code + chr((ord(text[Ord]) + ((-1) ** (Ord + Q)) * (s * Ord + key)) % 1424)
        else:
            return print('Присутствуют недопустимые символы! Один из таких:', text[Ord])
    with open(Directory, 'w+', encoding='utf-8') as txt:
        txt.write(code)
    if Q == 0:
        return print('Текст зашифрован! Полный ключ шифрования:', key, '_', s)
    if Q == 1:
        return print('Текст расшифрован!')


Directory = str(input('Укажите полный путь к текстовому файлу: '))
TxtFile = open(Directory, 'r', encoding='utf-8')
Q = int(input('Зашифровать (кнопка 0) | Расшифровать (кнопка 1): '))
if Q == 0:
    key = random.randint(1024, 16384)
    s = random.randint(2, 64)
    de_en_code(TxtFile.read())
if Q == 1:
    key = int(input('Введите основной ключ шифрования (это целое положительное число): '))
    s = int(input('Введите малый ключ шифрования (это целое положительное число): '))
    de_en_code(TxtFile.read())
