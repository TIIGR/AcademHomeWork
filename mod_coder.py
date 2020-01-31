RUS = '0123456789АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщъыьЭэЮюЯя .,!?"()@\#:-_–'


def de_en_code(text):
    code = ''
    error = 'Присутствуют недопустимые символы: '
    for Ord in range(0, len(text)):
        if text[Ord] not in RUS:
            error = error + text[Ord]
        if Q == 0 and text[Ord] in RUS:
            code = code + RUS[(RUS.index(text[Ord]) + ((-1) ** Ord) * (Ord + 1)) % len(RUS)]
        if Q == 1 and text[Ord] in RUS:
            code = code + RUS[(RUS.index(text[Ord]) - ((-1) ** Ord) * (Ord + 1)) % len(RUS)]
    if error == 'Присутствуют недопустимые символы: ':
        return code
    else:
        return error


Text = str(input('Введите текст: '))
Q = int(input('Зашифровать (кн. 0) | Расшифровать (кн. 1): '))
print(de_en_code(Text))
