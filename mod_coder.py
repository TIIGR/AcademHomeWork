RUS = '0123456789АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщъыьЭэЮюЯя .,!?"()@\#:-_–'


def de_en_code(text):
    code = 'Результат: '
    error = 'Присутствуют недопустимые символы: '
    for Ord in range(0, len(text)):
        if text[Ord] in RUS:
            code = code + RUS[(RUS.index(text[Ord]) + ((-1) ** (Ord + Q)) * (Ord + 1)) % len(RUS)]
        else:
            error = error + text[Ord]
    if error == 'Присутствуют недопустимые символы: ':
        return code
    else:
        return error


Text = str(input('Введите текст: '))
Q = int(input('Зашифровать (введите четное число) | Расшифровать (введите нечетное число): '))
print(de_en_code(Text))
