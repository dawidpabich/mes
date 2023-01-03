from math import sqrt

import numpy as np


class Element4():
    def __init__(self, integration_points):

        self.integration_points = integration_points
        self.ele4_rows = integration_points ** 2
        self.grid_ksi = [[0 for x in range(4)] for y in range(self.ele4_rows)]
        self.grid_eta = [[0 for x in range(4)] for y in range(self.ele4_rows)]
        self.N = [[0 for x in range(4)] for y in range(self.ele4_rows)]  # dla macierzy C
        self.data = []

    def calculate(self):

        if self.integration_points == 2:
            arg = 1 / sqrt(3)
            ksi_args = [-arg, arg, arg, -arg]
            eta_args = [-arg, -arg, arg, arg]
        elif self.integration_points == 3:
            arg = sqrt(3 / 5)
            ksi_args = [-arg, 0, arg, -arg, 0, arg, -arg, 0, arg]
            eta_args = [-arg, -arg, -arg, 0, 0, 0, arg, arg, arg]
        elif self.integration_points == 4:
            arg = 0.861136
            arg2 = 0.339981
            ksi_args = [-arg, -arg2, arg2, arg, -arg, -arg2, arg2, arg,
                        -arg, -arg2, arg2, arg, -arg, -arg2, arg2, arg]
            eta_args = [-arg, -arg, -arg, -arg, -arg2, -arg2, -arg2, -arg2,
                        arg2, arg2, arg2, arg2, arg, arg, arg, arg]
        for i in range(self.ele4_rows):
            # pochodne po ksi
            self.grid_ksi[i][0] = -0.25 * (1 - eta_args[i])
            self.grid_ksi[i][1] = 0.25 * (1 - eta_args[i])
            self.grid_ksi[i][2] = 0.25 * (1 + eta_args[i])
            self.grid_ksi[i][3] = -0.25 * (1 + eta_args[i])
            # pochodne po eta
            self.grid_eta[i][0] = -0.25 * (1 - ksi_args[i])
            self.grid_eta[i][1] = -0.25 * (1 + ksi_args[i])
            self.grid_eta[i][2] = 0.25 * (1 + ksi_args[i])
            self.grid_eta[i][3] = 0.25 * (1 - ksi_args[i])

        for i in range(self.ele4_rows):
            self.N[i][0] = 0.25 * (1 - ksi_args[i]) * (1 - eta_args[i])
            self.N[i][1] = 0.25 * (1 + ksi_args[i]) * (1 - eta_args[i])
            self.N[i][2] = 0.25 * (1 + ksi_args[i]) * (1 + eta_args[i])
            self.N[i][3] = 0.25 * (1 - ksi_args[i]) * (1 + eta_args[i])

        self.data.append(self.grid_ksi)
        self.data.append(self.grid_eta)

        return (self.data)


    def draw(self):
        print("KSI")
        for list in self.grid_ksi:
            for x in list:
                print(x, end=" ")
            print()

        print("\nETA")
        for list in self.grid_eta:
            for x in list:
                print(x, end=" ")
            print()