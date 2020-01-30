RUS = '0123456789АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщъыьЭэЮюЯя .,!?"()@/#:-_–'


def de_en_code(word):
    code = ''
    for Ord in range(0, len(word)):
        if word[Ord] not in RUS:
            exit('Присутствует недопустимый символ!')
        if Q == 0:
            ind = (RUS.index(word[Ord]) + ((-1) ** Ord) * (Ord + 1)) % 88
            code = code + RUS[ind]
        if Q == 1:
            ind = (RUS.index(word[Ord]) - ((-1) ** Ord) * (Ord + 1)) % 88
            code = code + RUS[ind]
    return code


Word = str(input('Введите текст: '))
Q = int(input('Зашифровать (кн. 0) | Расшифровать (кн. 1): '))
print(de_en_code(Word))
