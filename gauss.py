# --- исходные данные
myA = [
    [1.0, -2.0, 3.0, -4.0],
    [3.0, 3.0, -5.0, -1.0],
    [3.0, 0.0, 3.0, -10.0],
    [-2.0, 1.0, 2.0, -3.0]
]

myB = [
    2.0,
    -3.0,
    8.0,
    5.0]


# --- вывод системы на экран
def FancyPrint(a, b, selected):
    for row in range(len(b)):
        print("(", end='')
        for col in range(len(a[row])):
            print("\t{1:10.2f}{0}".format(" " if (selected is None or selected != (row, col)) else "*", a[row][col]),
                  end='')
        print("\t) * (\tX{0}) = (\t{1:10.2f})".format(row + 1, b[row]))


# --- перемена местами двух строк системы
def SwapRows(a, b, row1, row2):
    a[row1], a[row2] = a[row2], a[row1]
    b[row1], b[row2] = b[row2], b[row1]


# --- деление строки системы на число
def DivideRow(a, b, row, divider):
    a[row] = [c / divider for c in a[row]]
    b[row] /= divider


# --- сложение строки системы с другой строкой, умноженной на число
def CombineRows(a, b, row, source_row, weight):
    a[row] = [(c + k * weight) for c, k in zip(a[row], a[source_row])]
    b[row] += b[source_row] * weight


# --- решение системы методом Гаусса (приведением к треугольному виду)
def Gauss(a, b):
    column = 0
    while column < len(b):
        print("Ищем максимальный по модулю элемент в {0}-м столбце:".format(column + 1))
        current_row = None
        for r in range(column, len(a)):
            if current_row is None or abs(a[r][column]) > abs(a[current_row][column]):
                current_row = r
        if current_row is None:
            print("решений нет")
            return None
        FancyPrint(a, b, (current_row, column))
        if current_row != column:
            print("Переставляем строку с найденным элементом повыше:")
            SwapRows(a, b, current_row, column)
            FancyPrint(a, b, (column, column))
        print("Нормализуем строку с найденным элементом:")
        DivideRow(a, b, column, a[column][column])
        FancyPrint(a, b, (column, column))
        print("Обрабатываем нижележащие строки:")
        for r in range(column + 1, len(a)):
            CombineRows(a, b, r, column, -a[r][column])
        FancyPrint(a, b, (column, column))
        column += 1
    print("Матрица приведена к треугольному виду, считаем решение")
    X = [0 for b in b]
    for i in range(len(b) - 1, -1, -1):
        X[i] = b[i] - sum(x * a for x, a in zip(X[(i + 1):], a[i][(i + 1):]))
    print("Получили ответ:")
    print("\n".join("X{0} =\t{1:10.2f}".format(i + 1, x) for i, x in enumerate(X)))
    return X


print("Исходная система:")
FancyPrint(myA, myB, None)

print("Решаем:")
Gauss(myA, myB)
