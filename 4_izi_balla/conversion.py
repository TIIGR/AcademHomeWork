def conversion(value, old, new):
    if b < 2 or c < 2 or b > 36 or c > 36:
        return "Введенные вами сс, противоречат возможностям программы"
    else:
        if isinstance(value, str):
            n = int(value, old)
        else:
            n = int(value)
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < new:
            return alphabet[n]
        else:
            return conversion(n // new, old, new) + alphabet[n % new]


a = input("Введите число (от 0 до z): ")
b = int(input("Введите основание сс введенного числа (не превыш. 36): "))
c = int(input("Введите конечное основание сс (не превыш. 36): "))
print("Ответ: ", conversion(a, b, c))
