import numpy as np

from Data import Data
from Ele4 import Eleme4
from Jakobian import Jakobian
from MatrixH import MatrixH
from Agregate import *
from MatrixHBC import MatrixHBC
from Element4HBC import Element4HBC
from MatrixP import MatrixP


class Node:
    def __init__(self, ID, x, y):
        self.ID = ID
        self.x = x
        self.y = y
        self.BC = -1

    def __str__(self):
        return f'ID = {self.ID} x = {self.x}, y = {self.y}, BC = {self.BC}'

    def set_BC(self, node, BC_data):
        if node.ID in BC_data:
            node.BC = 1
        else:
            node.BC = 0


class Element:
    def __init__(self, ID, nodes_ID):
        self.ID = ID
        self.nodes_ID = nodes_ID[1:5]
        self.H = None
        self.Hbc = None
        self.P = None

    def __str__(self):
        return f'ID = {self.ID} nodes ID = {self.nodes_ID}'


class Grid:
    def __init__(self):
        self.data = Data("Test1_4_4.txt")
        self.nodes = []
        self.elements = []
        for it, node in enumerate(self.data.nodes_data):
            node = Node(self.data.nodes_data[it][0], self.data.nodes_data[it][1], self.data.nodes_data[it][2])
            node.set_BC(node, self.data.BC_data)
            self.nodes.append(node)

        for it, element in enumerate(self.data.elements_data):
            self.elements.append(Element(self.data.elements_data[it][0], self.data.elements_data[it]))

    def show(self):
        print('Nodes info')
        for node in self.nodes:
            print(node)

        print('\nElements info')
        for element in self.elements:
            print(element)


class GlobalData:
    def __init__(self, global_data_values):
        self.SimulationTime = global_data_values[0]
        self.SimulationStepTime = global_data_values[1]
        self.Conductivity = global_data_values[2]
        self.Alfa = global_data_values[3]
        self.Tot = global_data_values[4]
        self.InitialTemp = global_data_values[5]
        self.Density = global_data_values[6]
        self.SpecificHeat = global_data_values[7]

    def __str__(self):
        return (f'Global data info\n'
                f'Simulation time: {self.SimulationTime}\n'
                f'Simulation step time: {self.SimulationStepTime}\n'
                f'Conductivity: {self.Conductivity}\n'
                f'Alfa: {self.Alfa}\n'
                f'Tot: {self.Tot}\n'
                f'InitialTemp: {self.InitialTemp}\n'
                f'Density: {self.Density}\n'
                f'SpecificHeat: {self.SpecificHeat}\n')


def main():
    grid = Grid()
    global_data = GlobalData(grid.data.global_data_values)

    npc = 2
    element4 = Eleme4(npc)
    #element4.calculate()
    element4_data = element4.calculate()

    element4HBC = Element4HBC(npc, 300)
    element4HBC.calculate()



    for it, element in enumerate(grid.elements):
        print(f"ELEMENT {it }")
        jakob = Jakobian(element4_data, element.nodes_ID, grid.nodes, npc)

        matrixH = MatrixH(jakob.inv_jakob, element4_data, jakob.jakobs, npc)
        element.H = matrixH.H


        matrixHBC = MatrixHBC(element, grid.nodes, element4HBC, npc)
        element.Hbc = matrixHBC.HBC

        matrixP = MatrixP(element, grid.nodes, element4HBC, 300, 1200, 2)
       # print(matrixP.P)
        element.P = matrixP.P

        element.H += element.Hbc



        #print(element.H)


    H_aggregated = agregateH(grid)
    P_aggregated = agregateP(grid)

    print("H aggregated:")
    for x in H_aggregated:
       print(x)
    print("P aggregated:")
    for x in P_aggregated:
       print(x)
    print("//////////////")
    print(P_aggregated)
    print("//////////////")

    negative_P_aggregated = np.negative(P_aggregated)
    # Ax = B
    A = H_aggregated
    B = negative_P_aggregated
    print(np.linalg.solve(A, B))



main()


# grid = Grid()
# element4HBC = Element4HBC(2, 300)
# element4HBC.calculate()
# matrixP = MatrixP(grid.elements[0], grid.nodes, element4HBC, 25, 1200, 2)



