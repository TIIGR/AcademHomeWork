"""
This program does the job for me :)
"""
print('Введите 4-х значное число : ')
Y = int(input())
A = Y // 1000
B = (Y // 100) % 10
C = (Y // 10) % 10
D = Y % 10
Z = A + B + C + D
print('В этом числе:')
print(A, ' - тысяч ; ', B, ' - сотен ; ', C, ' - десятков ; ', D, ' - единиц . ')
print('Сумма разрядов числа равна : ', A, ' + ', B, ' + ', C, ' + ', D, ' = ', Z)
print('Перевертыш этого числа - ', D * 1000 + C * 100 + B * 10 + A)

