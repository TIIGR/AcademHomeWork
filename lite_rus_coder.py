rus = "0123456789АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя.,?!() "
eng = "akĕUĈDēĘĀpLrPxAčďonzcMXąĊJĐRęlĨĆċĜemjyiKĝVQăIwCOědShWĖćĒbBqČĂFsđėĉğfĔHvĎuYĞGĚĄātEgZ"


def encode(word):
    length = len(word)
    wod = ""
    for Ord in range(0, length):
        wod = wod + eng[rus.index(word[Ord])]
    return wod


def decode(word):
    length = len(word)
    wod = ""
    for Ord in range(0, length):
        wod = wod + rus[eng.index(word[Ord])]
    return wod


n = input("Введите закодированный (или обычный) текст, программа сама решит, что делать: ")
if n[0] in eng:
    print(decode(n))
if n[0] in rus:
    print(encode(n))
