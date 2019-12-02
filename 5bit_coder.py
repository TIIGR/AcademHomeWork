def encode(first):
    rus = "0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,?!()# "
    eng = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM "
    length = len(first)
    degree = length - 1
    number = 0
    wod = ""
    for ord in range(0, length):
        code = rus.index(first[ord])
        number = number + (code * (51 ** degree))
        degree = degree - 1
    if number == 0:
        return 0
    else:
        while number != 0:
            nome = number % 50
            wod = wod + eng[nome]
            number = number // 50
        return wod

def decode(word):
    rus = "0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,?!()# "
    eng = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM "
    length = len(word)
    degree = 0
    number = 0
    wod = ""
    for ord in range(0, length):
        code = eng.index(word[ord])
        number = number + (code * (50 ** degree))
        degree = degree + 1
    if number == 0:
        return 0
    else:
        while number != 0:
            nome = number % 51
            wod = wod + rus[nome]
            number = number // 51
        inverse = wod[::-1]
        return inverse


Q = int(input("Декодировать (tap 0) или закодировать (tap 1) текст? "))
if Q == 0:
    n = str(input("Декодировать текст: "))
    print(decode(n))
if Q == 1:
    n = str(input("Закодировать текст: "))
    print(encode(n))
