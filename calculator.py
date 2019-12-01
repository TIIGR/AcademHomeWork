def convert_base(num, to_base, from_base):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // from_base, to_base, from_base) + alphabet[n % to_base]


convert_base(14, 5, 10)
