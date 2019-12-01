def carry(value, base):
    if isinstance(value, str):
        n = int(value)
    else:
        n = int(value)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < base:
        return alphabet[n]
    else:
        return carry(n // base, base) + alphabet[n % base]


a = int(input("Введите число в 10 сс: "))
c = int(input("Введите основание конечной системы счисления: "))
print(carry(a, c))
