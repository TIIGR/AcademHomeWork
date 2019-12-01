def Prime(n):
    if n == 1:
        return "True"
    else:
        d = 2
        while n % d != 0:
            d += 1
        return d == n
    

a = int(input("Введите число: "))
print(Prime(a))
