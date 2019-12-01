def convert(value, old, new):
    if b <= 1 or c <= 1 or b > 36 or c > 36:
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
            return convert(n // new, old, new) + alphabet[n % new]


a = input("Введите число (от 0 до Z): ")
b = int(input("Введите основание сс введенного числа (не превыш. 36): "))
c = int(input("Введите конечное основание сс (не превыш. 36): "))
print(convert(a, b, c))
