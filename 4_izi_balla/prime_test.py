def prime(n):
    if n == 1:
        return ()
    if n == 2:
        return True
    for i in range(2, round(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


print(prime(100500))
