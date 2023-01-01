import numpy as np


class MatrixH:
    def __init__(self, inverted_jakob, ele4_data, k, detJ, npc):

        self.inverted_jakob = inverted_jakob
        self.ele4_data = ele4_data
        self.k = k
        self.detJ = detJ
        self.dNdx = []
        self.dNdy = []
        self.Hpc = []
        self.H = np.zeros((4, 4))

        self.calculate(npc)

    def calculate(self, npc):
        if npc == 2:
            w = [[1, 1], [1, 1]]
            wPC = []
            for i in range(npc):
                for j in range(npc):
                    wPC.append(w[0][i] * w[1][j])

        elif npc == 3:
            w = [[5 / 9, 8 / 9, 5 / 9], [5 / 9, 8 / 9, 5 / 9]]
            wPC = []
            for i in range(npc):
                for j in range(npc):
                    wPC.append(w[0][i] * w[1][j])

        elif npc == 4:
            w = [[0.347855, 0.652145, 0.652145, 0.347855], [0.347855, 0.652145, 0.652145, 0.347855]]
            wPC = []
            for i in range(npc):
                for j in range(npc):
                    wPC.append(w[0][i] * w[1][j])


        ksi_data = self.ele4_data[0]
        eta_data = self.ele4_data[1]
        print(self.detJ)
        print(len(wPC), wPC)
        for i in range(npc ** 2):
            self.dNdx.append([])
            self.dNdy.append([])

        for i in range(npc ** 2):
            x = 1 / self.detJ[i]
            for j in range(4):
                self.dNdx[i].append(
                    (x * self.inverted_jakob[i][1][1] * ksi_data[i][j]) + (x * (-self.inverted_jakob[i][0][1])) * eta_data[i][j])
                print(x, x * self.inverted_jakob[i][1][1], ksi_data[i][j], x * (-self.inverted_jakob[i][0][1]), eta_data[i][j], x * self.inverted_jakob[i][1][1] * ksi_data[i][j], x * (-self.inverted_jakob[i][0][1]) * eta_data[i][j], x * self.inverted_jakob[i][1][1] * ksi_data[i][j] + (x * (-self.inverted_jakob[i][0][1])) * eta_data[i][j])
                print(x * self.inverted_jakob[i][0][0], x * self.inverted_jakob[i][0][1], x * self.inverted_jakob[i][1][0], x * self.inverted_jakob[i][1][1])
                self.dNdy[i].append(
                    (x * (-self.inverted_jakob[i][1][0]) * ksi_data[i][j]) + (x * self.inverted_jakob[i][0][0] * eta_data[i][j]))
                # self.dNdx[i].append(
                #     self.inverted_jakob[i][1][1] * ksi_data[i][j] + self.inverted_jakob[i][1][0] * eta_data[i][j])
                #
                # self.dNdy[i].append(
                #     self.inverted_jakob[i][0][1] * ksi_data[i][j] + self.inverted_jakob[i][0][0] * eta_data[i][j])

        for i in range(npc ** 2):
            dN_po_dx = np.array(self.dNdx[i])
            dN_po_dx_transponowane = np.reshape(dN_po_dx, (4, 1))
            temp1 = dN_po_dx * dN_po_dx_transponowane


            dN_po_dy = np.array(self.dNdy[i])
            dN_po_dy_transponowane = np.reshape(dN_po_dy, (4, 1))
            temp2 = dN_po_dy * dN_po_dy_transponowane

            self.H += (temp1 + temp2) * self.k * self.detJ[i] * wPC[i]
            # print(f"H LOCAL {i}\n {(temp1 + temp2) * self.k * self.detJ[i] * wPC[i]}")
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

        print("H: ")
        print(self.H)
