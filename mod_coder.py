RUS = '0123456789АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщъыьЭэЮюЯя .,!?"()@\#:-_–'


def de_en_code(text):
    error = 'Присутствуют недопустимые символы: '
    code = ''
    for Ord in range(0, len(text)):
        if text[Ord] not in RUS:
            for bug in range(Ord, len(text)):
                if text[bug] not in RUS:
                    error = error + text[bug]
            exit(error)
        if Q == 0:
            ind = (RUS.index(text[Ord]) + ((-1) ** Ord) * (Ord + 1)) % len(RUS)
            code = code + RUS[ind]
        if Q == 1:
            ind = (RUS.index(text[Ord]) - ((-1) ** Ord) * (Ord + 1)) % len(RUS)
            code = code + RUS[ind]
    return code


Text = str(input('Введите текст: '))
Q = int(input('Зашифровать (кн. 0) | Расшифровать (кн. 1): '))
print(de_en_code(Text))
