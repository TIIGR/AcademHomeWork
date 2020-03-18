from numpy import array as arr
from numba import njit

AB = arr([
    [1.5, 2.0, 1.5, 5.0],
    [3.0, 2.0, 4.0, 6.0],
    [1.0, 6.0, 0.0, 7.0]
])


@njit
def v_gauss_jit(ab: arr) -> arr:
    ab = ab.copy()
    n = len(ab)

    for k in range(n):
        for i in range(k + 1, n):
            ab[k] /= ab[k][k]
            ab[i] -= ab[k] * (ab[i][k])
    ab[n - 1] /= ab[n - 1][n - 1]
    pass

    for i in range(n):
        for j in range(i + 1, n):
            ab[i] -= ab[j] * ab[i][j]
    pass

    x = []
    for i in range(n):
        x.append(round(ab[i][n] * 10 ** 10) * 10 ** -10)

    return x


def v_gauss_no_jit(ab: arr) -> arr:
    ab = ab.copy()
    n = len(ab)

    for k in range(n):
        for i in range(k + 1, n):
            ab[k] /= ab[k][k]
            ab[i] -= ab[k] * (ab[i][k])
    ab[n - 1] /= ab[n - 1][n - 1]
    pass

    for i in range(n):
        for j in range(i + 1, n):
            ab[i] -= ab[j] * ab[i][j]
    pass

    x = []
    for i in range(n):
        x.append(ab[i][n])

    return x


print(v_gauss_jit(AB))
print(v_gauss_no_jit(AB))
