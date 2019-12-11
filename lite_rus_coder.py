rus = "(.!0БойЙкАсбЁВО4цНжХЩъ2эЪ5фяуеСдшИЕмЗЬпПЫрЛ9ыФлгШёхвз3тн7Ящ1ЮЖКУГ6иьЧч8ЦаЭМРюДТ?,) "
eng = "akĕUĈDēĘĀpLrPxčďAonzcMXąĊJĐRęlĨĆċĜemjyiKĝVQăIwCOědShWĖćĒbBqČĂFsđėĉğfĔHvĎuYĞGĚĄātEgZ"


def encode(word):
    code = ""
    for Ord in word:
        if Ord in rus:
            code = code + eng[rus.index(Ord)]
        else:
            exit('Недопустимый ввод!')
    return code


def decode(code):
    word = ""
    for Ord in code:
        if Ord in eng:
            word = word + rus[eng.index(Ord)]
        else:
            exit('Недопустимый ввод!')
    return word


n = input("Введите закодированный (или обычный) текст, программа сама решит, что делать: ")
if n[0] in rus:
    print(encode(n))
else:
    print(decode(n))
