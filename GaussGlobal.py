from math import sqrt


class Gauss():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self, liczba_punktow_calkowania, f):
        wezly = []
        wagi = []
        N1 = []
        N2 = []
        xpc = []
        fxpc = []
        suma = 0

        if liczba_punktow_calkowania == 2:
            wezly = [(-1 / (3 ** (1 / 2))), (1 / (3 ** (1 / 2)))]
            wagi = [1, 1]
        elif liczba_punktow_calkowania == 3:
            wezly = [-sqrt(3 / 5), 0, (3 / 5) ** (1 / 2)]
            wagi = [5 / 9, 8 / 9, 5 / 9]
        elif liczba_punktow_calkowania == 4:
            wezly = [-0.861136, -0.339981, 0.339981, 0.861136]
            wagi = [0.347855, 0.652145, 0.652145, 0.347855]
        elif liczba_punktow_calkowania == 5:
            wezly = [-0.906180, -0.538469, 0, 0.538469, 0.906180]
            wagi = [0.236927, 0.478269, 0.568889, 0.478269, 0.236927]

        for i in range(liczba_punktow_calkowania):
            N1.append((1 - wezly[i]) / 2)
            N2.append((1 + wezly[i]) / 2)

        for i in range(liczba_punktow_calkowania):
            xpc.append(N1[i] * self.a + N2[i] * self.b)

        for i in range(liczba_punktow_calkowania):
            fxpc.append(f(xpc[i]))
            suma += f(xpc[i]) * wagi[i]

        suma = suma * abs(((self.b - self.a) / 2))
        print(xpc, fxpc, suma)
