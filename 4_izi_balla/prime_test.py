def Prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


a = int(input("Введите число: "))
print(Prime(a))
