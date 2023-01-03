import numpy as np


class MatrixC:

    def __init__(self, element4, detJ, ro, cp, npc):
        self.C = np.zeros((4, 4))
        self.element4 = element4
        self.detJ = detJ
        self.ro = ro
        self.cp = cp
        self.npc = npc

        self.calculate()

    def calculate(self):
        if self.npc == 2:
            w = [[1, 1], [1, 1]]
            wPC = []
            for i in range(self.npc):
                for j in range(self.npc):
                    wPC.append(w[0][i] * w[1][j])

        elif self.npc == 3:
            w = [[5 / 9, 8 / 9, 5 / 9], [5 / 9, 8 / 9, 5 / 9]]
            wPC = []
            for i in range(self.npc):
                for j in range(self.npc):
                    wPC.append(w[0][i] * w[1][j])

        elif self.npc == 4:
            w = [[0.347855, 0.652145, 0.652145, 0.347855], [0.347855, 0.652145, 0.652145, 0.347855]]
            wPC = []
            for i in range(self.npc):
                for j in range(self.npc):
                    wPC.append(w[0][i] * w[1][j])


        for i in range(self.npc ** 2):
            N = np.array(self.element4.N[i])
            N_Transponowane = np.reshape(N, (4, 1))
            N_Razy_N_Transponowane = N * N_Transponowane
            N_Razy_N_Transponowane *= self.detJ[i] * self.ro * self.cp
            self.C += N_Razy_N_Transponowane * wPC[i]


