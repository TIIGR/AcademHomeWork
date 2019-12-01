def calc(num, base, target):
    if b <= 0 or c <= 0 or b > 36 or c > 36:
        return "Введенные вами сс, противоречат возможностям программы"
    else:
        if isinstance(num, str):
            n = int(num, base)
        else:
            n = int(num)
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < target:
            return alphabet[n]
        else:
            return calc(n // target, base, target) + alphabet[n % target]


a = input("Введите число: ")
b = int(input("Введите основание сс введенного числа (не превыш. 36): "))
c = int(input("Введите конечное основание сс (не превыш. 36): "))
print(calc(a, b, c))
