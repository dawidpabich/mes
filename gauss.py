def f1(x):
    return (2 * x * x) + (3 * x) - 8


def f2(x, y):
    return (-5 * x * x * y) + (2 * x * y * y) + 10


def gauss_1D_2P():
    suma = 0
    punkt_calkowania = [(-1 / (3 ** (1 / 2))), (1 / (3 ** (1 / 2)))]
    waga = [1, 1]
    for i in range(len(punkt_calkowania)):
        suma += f1(punkt_calkowania[i]) * waga[i]
    return suma

def gauss_1D_3P():
    suma = 0
    punkt_calkowania = [-(3 / 5) ** (1 / 2), 0, (3 / 5) ** (1 / 2)]
    waga = [5 / 9, 8 / 9, 5 / 9]
    for i in range(len(punkt_calkowania)):
        suma += f1(punkt_calkowania[i]) * waga[i]
    return suma

def gauss_2D_2P():
    suma = 0
    punkt_calkowania = [(-1 / (3 ** (1 / 2))), (1 / (3 ** (1 / 2)))]
    waga = [1, 1]
    for i in range(len(punkt_calkowania)):
        for j in range(len(punkt_calkowania)):
            suma += f2(punkt_calkowania[i], punkt_calkowania[j]) * waga[i] * waga[j]

    return suma

def gauss_2D_3P():
    suma = 0
    punkt_calkowania = [-(3 / 5) ** (1 / 2), 0, (3 / 5) ** (1 / 2)]
    waga = [5 / 9, 8 / 9, 5 / 9]
    for i in range(len(punkt_calkowania)):
        for j in range(len(punkt_calkowania)):
            suma += f2(punkt_calkowania[i], punkt_calkowania[i]) * waga[i] * waga[j]


    return suma