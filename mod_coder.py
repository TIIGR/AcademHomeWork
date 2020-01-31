RUS = '0123456789АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщъыьЭэЮюЯя .,!?"()@\#:-_–'


def de_en_code(text):
    code = ''
    error = 'Присутствуют недопустимые символы: '
    for Ord in range(0, len(text)):  # Использование "for Ord in Text:" привело бы к неправильному шифрованию
        if text[Ord] in RUS:         # текста в некоторых случаях (нарушению индексов символов)
            code = code + RUS[(RUS.index(text[Ord]) + ((-1) ** (Ord + Q)) * (Ord + 1)) % len(RUS)]
        else:
            error = error + text[Ord]
    if error == 'Присутствуют недопустимые символы: ':
        return code
    else:
        return error


Text = str(input('Введите текст: '))
Q = int(input('Зашифровать (введите четное число) | Расшифровать (введите нечетное число): '))
print(de_en_code(Text))  # Если эту функцию применять {N * len(RUS) - 1} раз, получится исходный текст (N - нат. число)
