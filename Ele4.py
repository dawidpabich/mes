from math import sqrt

import numpy as np


class Eleme4():
    def __init__(self, integration_points):

        self.integration_points = integration_points
        self.ele4_rows = integration_points ** 2
        self.grid_ksi = [[0 for x in range(4)] for y in range(self.ele4_rows)]
        self.grid_eta = [[0 for x in range(4)] for y in range(self.ele4_rows)]
        self.N = [] # dla macierzy C
        self.NTransponowane = None
        self.data = []



    def calculate(self):

        if self.integration_points == 2:
            arg = 1 / sqrt(3)
            ksi_args = [-arg, -arg, arg, arg]
            eta_args = [-arg, arg, arg, -arg]
        elif self.integration_points == 3:
            arg = sqrt(3 / 5)
            ksi_args = [-arg, -arg, -arg, 0, 0, 0, arg, arg, arg]
            eta_args = [-arg, 0, arg, -arg, 0, arg, -arg, 0, arg]

        elif self.integration_points == 4:
            arg = 0.861136
            arg2 = 0.339981
            ksi_args = [-arg, -arg, -arg, -arg, -arg2, -arg2, -arg2, -arg2,
                             arg2, arg2, arg2, arg2, arg, arg, arg, arg]
            eta_args = [-arg, -arg2, arg2, arg, -arg, -arg2, arg2, arg,
                             -arg, -arg2, arg2, arg, -arg, -arg2, arg2, arg]

        for i in range(self.ele4_rows):
            self.grid_ksi[i][0] = -0.25 * (1 - ksi_args[i])
            self.grid_ksi[i][1] = 0.25 * (1 - ksi_args[i])
            self.grid_ksi[i][2] = 0.25 * (1 + ksi_args[i])
            self.grid_ksi[i][3] = -0.25 * (1 + ksi_args[i])

            self.grid_eta[i][0] = -0.25 * (1 - eta_args[i])
            self.grid_eta[i][1] = -0.25 * (1 + eta_args[i])
            self.grid_eta[i][2] = 0.25 * (1 + eta_args[i])
            self.grid_eta[i][3] = 0.25 * (1 - eta_args[i])

        #     self.N.append([])
        #     ksi = ksi_args[i]
        #     eta = eta_args[i]
        #     N1 = 0.25 * (1 + ksi) * (1 + eta)
        #     N2 = 0.25 * (1 - ksi) * (1 + eta)
        #     N3 = 0.25 * (1 - ksi) * (1 - eta)
        #     N4 = 0.25 * (1 + ksi) * (1 - eta)
        #     self.N[i].append(N1)
        #     self.N[i].append(N2)
        #     self.N[i].append(N3)
        #     self.N[i].append(N4)
        #
        # for j in range(self.ele4_rows):
        #     tempN = np.array(self.N[j])
        #     NTransponowane = np.reshape(tempN, (4, 1))
        #     NRazyNTransponowane = tempN * NTransponowane
        #     print(NRazyNTransponowane)




        self.data.append(self.grid_ksi)
        self.data.append(self.grid_eta)
        #self.draw()
        return(self.data)
        #print(self.data[1])


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




