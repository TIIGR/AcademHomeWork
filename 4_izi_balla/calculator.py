def carry(value, original):
    if isinstance(value, str):
        n = int(value)
    else:
        n = int(value)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < original:
        return alphabet[n]
    else:
        return carry(n // original, original) + alphabet[n % original]


a = int(input("Введите число в 10 сс: "))
c = int(input("Введите основание конечной системы счисления: "))
print(carry(a, c))
