_fib_cache = {1: 1, 2: 1}

n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)
def mem_fib(n):
    result = _fib_cache.get(n)
    if result is None:
        result = mem_fib(n-2) + mem_fib(n-1)
        _fib_cache[n] = result
    return result

print('Ответ: ', mem_fib(n))
