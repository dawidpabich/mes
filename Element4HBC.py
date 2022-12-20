from math import sqrt

import numpy as np


class Element4HBC():
    def __init__(self, npc, alfa):

        self.npc = npc
        self.alfa = alfa

        self.dolna_sciana = []
        self.prawa_sciana = []
        self.gorna_sciana = []
        self.lewa_sciana = []

        self.dolna_sciana_N_Razy_NTransponowane = np.zeros((4, 4))
        self.prawa_sciana_N_Razy_NTransponowane = np.zeros((4, 4))
        self.gorna_sciana_N_Razy_NTransponowane = np.zeros((4, 4))
        self.lewa_sciana_N_Razy_NTransponowane = np.zeros((4, 4))

        for i in range(npc):
            self.dolna_sciana.append([])
            self.lewa_sciana.append([])
            self.prawa_sciana.append([])
            self.gorna_sciana.append([])

    def calculate(self):
        arg = 1 / sqrt(3)

        if self.npc == 2:
            wagi = [1, 1]
            arg = 0.5773
            # PC1 = [ (arg, -1), (-arg, -1)] # dolna
            # PC2 = [(1, arg), (1, -arg)] # prawa
            # PC3 = [(arg, 1), (-arg, 1)] # gorna
            # PC4 = [(-1, arg), (-1, -arg)] # lewa
            PC1 = [(-arg, -1), (arg, -1)]  # dolna
            PC2 = [(1, -arg), (1, arg)]  #
            PC3 = [(-arg, 1), (arg, 1)]
            PC4 = [(-1, -arg), (-1, arg)]

        # liczenie funkcji kształtu dla punktów całkowania
        for j in range(self.npc):
            """
            N1 = 0.25 * (1 - ksi) * (1 - eta)
            N2 = 0.25 * (1 + ksi) * (1 - eta)
            N3 = 0.25 * (1 + ksi) * (1 + eta)
            N4 = 0.25 * (1 - ksi) * (1 + eta)
            """
            """
            ???
                        N1 = 0.25 * (1 + ksi) * (1 + eta)
                        N2 = 0.25 * (1 - ksi) * (1 + eta)
                        N3 = 0.25 * (1 - ksi) * (1 - eta)
                        N4 = 0.25 * (1 + ksi) * (1 - eta)
            """

            # dolna - PC1
            ksi = PC1[j][0]
            eta = PC1[j][1]
            N1 = 0
            N2 = 0
            N3 = 0.25 * (1 - ksi) * (1 - eta)
            N4 = 0.25 * (1 + ksi) * (1 - eta)
            self.dolna_sciana[j].append(N1)
            self.dolna_sciana[j].append(N2)
            self.dolna_sciana[j].append(N3)
            self.dolna_sciana[j].append(N4)

            # prawa - PC2
            ksi = PC2[j][0]
            eta = PC2[j][1]
            N1 = 0.25 * (1 + ksi) * (1 + eta)
            N2 = 0
            N3 = 0
            N4 = 0.25 * (1 + ksi) * (1 - eta)
            self.prawa_sciana[j].append(N1)
            self.prawa_sciana[j].append(N2)
            self.prawa_sciana[j].append(N3)
            self.prawa_sciana[j].append(N4)

            # gorna - PC3
            ksi = PC3[j][0]
            eta = PC3[j][1]
            N1 = 0.25 * (1 + ksi) * (1 + eta)
            N2 = 0.25 * (1 - ksi) * (1 + eta)
            N3 = 0
            N4 = 0
            self.gorna_sciana[j].append(N1)
            self.gorna_sciana[j].append(N2)
            self.gorna_sciana[j].append(N3)
            self.gorna_sciana[j].append(N4)

            # lewa - PC4
            ksi = PC4[j][0]
            eta = PC4[j][1]
            N1 = 0
            N2 = 0.25 * (1 - ksi) * (1 + eta)
            N3 = 0.25 * (1 - ksi) * (1 - eta)
            N4 = 0

            self.lewa_sciana[j].append(N1)
            self.lewa_sciana[j].append(N2)
            self.lewa_sciana[j].append(N3)
            self.lewa_sciana[j].append(N4)
            # print(N1, N2)

        # liczenie N * N transponowane dla każdej ściany
        for i in range(self.npc):
            temp_dolna_sciana = np.array(self.dolna_sciana[i])
            temp_dolna_scianaT = temp_dolna_sciana.reshape((-1, 1))  # -1 znaczy - tyle wierszy ile potrzeba
            temp_N_razy_NTransponowane = np.multiply(temp_dolna_sciana, temp_dolna_scianaT)
            temp_N_razy_NTransponowane *= wagi[i] * self.alfa
            self.dolna_sciana_N_Razy_NTransponowane += temp_N_razy_NTransponowane

            temp_prawa_sciana = np.array(self.prawa_sciana[i])
            temp_prawa_scianaT = temp_prawa_sciana.reshape((-1, 1))  # -1 znaczy - tyle wierszy ile potrzeba
            temp_N_razy_NTransponowane = np.multiply(temp_prawa_sciana, temp_prawa_scianaT)
            temp_N_razy_NTransponowane *= wagi[i] * self.alfa
            self.prawa_sciana_N_Razy_NTransponowane += temp_N_razy_NTransponowane

            temp_gorna_sciana = np.array(self.gorna_sciana[i])
            temp_gorna_scianaT = temp_gorna_sciana.reshape((-1, 1))  # -1 znaczy - tyle wierszy ile potrzeba
            temp_N_razy_NTransponowane = np.multiply(temp_gorna_sciana, temp_gorna_scianaT)
            temp_N_razy_NTransponowane *= wagi[i] * self.alfa
            self.gorna_sciana_N_Razy_NTransponowane += temp_N_razy_NTransponowane

            temp_lewa_sciana = np.array(self.lewa_sciana[i])
            temp_lewa_scianaT = temp_lewa_sciana.reshape((-1, 1))  # -1 znaczy - tyle wierszy ile potrzeba
            temp_N_razy_NTransponowane = np.multiply(temp_lewa_sciana, temp_lewa_scianaT)
            temp_N_razy_NTransponowane *= wagi[i] * self.alfa
            self.lewa_sciana_N_Razy_NTransponowane += temp_N_razy_NTransponowane

    def draw(self):
        print("Dolna sciana")
        for list in self.dolna_sciana:
            for x in list:
                print(x, end=" ")
            print()

        print("Prawa sciana")
        for list in self.prawa_sciana:
            for x in list:
                print(x, end=" ")
            print()

        print("Gorna sciana")
        for list in self.gorna_sciana:
            for x in list:
                print(x, end=" ")
            print()

        print("Lewa sciana")
        for list in self.lewa_sciana:
            for x in list:
                print(x, end=" ")
            print()
