from math import sqrt

import numpy as np


class MatrixP:
    def __init__(self, element, nodes, element4MatrixHBC, alfa, tot, npc):
        self.alfa = alfa
        self.tot = tot
        self.npc = npc
        self.nodesID = element.nodes_ID
        self.nodes = nodes
        self.P = np.zeros((4, 1))
        self.element4MatrixHBC = element4MatrixHBC

        self.calculate()

    def calculate(self):

        detJ = 0
        HPCsc1 = np.zeros((4, 1))
        HPCsc2 = np.zeros((4, 1))
        HPCsc3 = np.zeros((4, 1))
        HPCsc4 = np.zeros((4, 1))

        for i in range(-1, 3):  # sprawdzamy każdą ścianę
            if (self.nodes[self.nodesID[i] - 1]).BC == 1 and (self.nodes[self.nodesID[i + 1] - 1]).BC == 1:

                x1 = self.nodes[self.nodesID[i] - 1].x
                x2 = self.nodes[self.nodesID[i + 1] - 1].x
                y1 = self.nodes[self.nodesID[i] - 1].y
                y2 = self.nodes[self.nodesID[i + 1] - 1].y

                # if(x1 - x2 != 0):
                #     detJ = (x1 - x2) / 2
                # else:
                #     detJ = (y1 - y2) / 2

                detJ = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) / 2
                # detJ = 0.0125
                if i == -1:  # prawa sciana
                    for j in range(self.npc):
                        N = self.element4MatrixHBC.prawa_sciana[j]

                        N = np.reshape(N, (4, 1))  # zmiana z wiersza w kolumne
                        N *= self.tot
                        HPCsc1 += N

                if i == 0:  # gorna sciana
                    for j in range(self.npc):
                        N = self.element4MatrixHBC.gorna_sciana[j]

                        N = np.reshape(N, (4, 1))  # zmiana z wiersza w kolumne
                        N *= self.tot
                        HPCsc2 += N

                if i == 1:  # lewa sciana
                    for j in range(self.npc):
                        N = self.element4MatrixHBC.lewa_sciana[j]

                        N = np.reshape(N, (4, 1))  # zmiana z wiersza w kolumne
                        N *= self.tot
                        HPCsc3 += N

                if i == 2:  # dolna sciana
                    for j in range(self.npc):
                        N = self.element4MatrixHBC.dolna_sciana[j]

                        N = np.reshape(N, (4, 1))  # zmiana z wiersza w kolumne
                        N *= self.tot
                        HPCsc4 += N
        self.P += HPCsc1 + HPCsc2 + HPCsc3 + HPCsc4
        self.P *= self.alfa * detJ  # det J gdzies indziej???

    def draw(self):
        for x in self.HBC:
            print(x)
        """for i in range(len(self.HBC)):
            print("HBC_local" + str(i + 1))
            for list in self.HBC[i]:
                for x in list:
                    print(x, end=" ")
                print()
            print()"""

        # print(self.elementHBpc[1])
    # print(np.array(self.elementHBpc[1]) * 25)
