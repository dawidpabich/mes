from math import sqrt

import numpy as np



class MatrixHBC:
    def __init__(self, element, nodes, element4MatrixHBC,  npc):
        self.npc = npc
        self.nodesID = element.nodes_ID
        self.nodes = nodes
        self.HBC = np.zeros((4,4))
        self.element4MatrixHBC = element4MatrixHBC

        self.calculate()


    def calculate(self):

        detJ = 0
        HBCpc = np.zeros((4, 4))

        for i in range (-1, 3): # sprawdzamy każdą ścianę
            if (self.nodes[self.nodesID[i] - 1]).BC == 1 and (self.nodes[self.nodesID[i + 1] - 1]).BC == 1:

                x1 = abs((self.nodes[self.nodesID[i] - 1]).x)
                x2 = abs((self.nodes[self.nodesID[i + 1] - 1]).x)
                y1 = abs((self.nodes[self.nodesID[i] - 1]).y)
                y2 = abs((self.nodes[self.nodesID[i + 1] - 1]).y)

                detJ = sqrt((x1-x2)**2 + (y1-y2)**2) / 2

                if i == -1: # prawa sciana
                    HBCpc += self.element4MatrixHBC.prawa_sciana_N_Razy_NTransponowane

                if i == 0: # gorna sciana
                    HBCpc += self.element4MatrixHBC.gorna_sciana_N_Razy_NTransponowane


                if i == 1: # lewa sciana
                    HBCpc += self.element4MatrixHBC.lewa_sciana_N_Razy_NTransponowane


                if i == 2: # dolna sciana
                    HBCpc += self.element4MatrixHBC.dolna_sciana_N_Razy_NTransponowane



        self.HBC += HBCpc * detJ # czy tutaj detJ???
        # print(self.HBC)
        # print()




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



        #print(self.elementHBpc[1])
       # print(np.array(self.elementHBpc[1]) * 25)



