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
        for i in range(self.npc ** 2):
            N = np.array(self.element4.N[i])
            N_Transponowane = np.reshape(N, (4, 1))

            N_Razy_N_Transponowane = N * N_Transponowane
            N_Razy_N_Transponowane *= self.detJ[i] * self.ro * self.cp
            self.C += N_Razy_N_Transponowane
