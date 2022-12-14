
import numpy as np


class MatrixH():
    def __init__(self, inverted_jakob, ele4_data, detJ, npc):

        self.inverted_jakob = inverted_jakob
        self.ele4_data = ele4_data
        self.k = 25
        self.detJ = detJ
        self.dNdx = []
        self.dNdy = []
        self.Hpc = []
        self.H = np.zeros((4,4))

        self.calculate(npc)

    def calculate(self, npc):
        ksi_data = self.ele4_data[0]
        eta_data = self.ele4_data[1]

        for i in range(npc ** 2):
            self.dNdx.append([])
            self.dNdy.append([])
            self.Hpc.append([ [], [], [], [] ])

        for i in range(npc ** 2):
            for j in range(4):
                self.dNdx[i].append(
                    self.inverted_jakob[i][0][0] * ksi_data[i][j] + self.inverted_jakob[i][1][0] * eta_data[i][j])

                self.dNdy[i].append(
                    self.inverted_jakob[i][0][1] * ksi_data[i][j] + self.inverted_jakob[i][1][1] * eta_data[i][j])



        for i in range(npc ** 2):
            for j in range(4):
                for k in range(4):
                    tempX = self.dNdx[i][j] * self.dNdx[i][k]
                    tempY = self.dNdy[i][j] * self.dNdy[i][k]
                    self.Hpc[i][j].append(self.k * (tempX + tempY) * self.detJ[j] )



        # sumowanie macierzy H
        if npc == 2:
            w = [[1, 1], [1, 1]]
            wPC = []
            for i in range(npc):
                for j in range(npc):
                    wPC.append(w[0][i] * w[1][j])

        elif npc == 3:
            w = [[ 5/9, 8/9, 5/9], [ 5/9, 8/9, 5/9]]
            wPC = []
            for i in range (npc):
                for j in range(npc):
                    wPC.append(w[0][i] * w[1][j])

        elif npc == 4:
            w = [[0.347855, 0.652145, 0.652145, 0.347855], [0.347855, 0.652145, 0.652145, 0.347855]]
            wPC = []
            for i in range (npc):
                for j in range(npc):
                    wPC.append(w[0][i] * w[1][j])


        for i in range(len(self.Hpc)):
            self.Hpc[i] = np.array(self.Hpc[i])
            self.Hpc[i] = self.Hpc[i] * wPC[i]

        for i in range(len(self.Hpc)):
            self.H = self.H + self.Hpc[i]
        #self.H = self.H.tolist()

        """for HpcIndex in range(len(self.Hpc)):
            print("Hpc" + str(HpcIndex + 1))
            for list in self.Hpc[HpcIndex]:
                for x in list:
                    print(x, end=" ")
                print()
            print()"""

        #self.draw()





    def draw(self):
        print("dNdX: ")
        for list in self.dNdx:
            for x in list:
                print(x, end=" ")
            print()

        print("dNdY: ")
        for list in self.dNdy:
            for x in list:
                print(x, end=" ")
            print()

        for HpcIndex in range(len(self.Hpc)):
            print("Hpc" + str(HpcIndex + 1))
            for list in self.Hpc[HpcIndex]:
                for x in list:
                    print(x, end=" ")
                print()
            print()

        print("H: ")
        print(self.H)






