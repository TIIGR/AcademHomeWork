rus = "0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,?!()# "
eng = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSUVWXYZ"
def encode(first):
    length = len(first)
    degree = length - 1
    number = 0
    wod = ""
    for ord in range(0, length):
        code = rus.index(first[ord])
        number = number + (code * (51 ** degree))
        degree = degree - 1
    while number != 0:
        nome = number % 50
        wod = wod + eng[nome]
        number = number // 50
    return wod

def decode(word):
    length = len(word)
    degree = 0
    number = 0
    wod = ""
    for ord in range(0, length):
        code = eng.index(word[ord])
        number = number + (code * (50 ** degree))
        degree = degree + 1
    while number != 0:
        nome = number % 51
        wod = wod + rus[nome]
        number = number // 51
    wod = wod[::-1]
    return wod


n = input("Введите закодированный (или обычный) текст, программа сама решит, что делать: ")
if n[0] in eng:
    print(decode(n))
if n[0] in rus:
    print(encode(n))
