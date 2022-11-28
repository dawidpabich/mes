from gauss import *
from gauss_better import Gauss
from Ele4 import Eleme4
from Jakobian import Jakobian
from MatrixH import MatrixH
from Agregate import agregate2D

def read_file(filename):
    file_data = []
    nodes_data = []
    elements_data = []

    with open(filename, 'r') as f:
        global_data_values = [int(next(f).split()[-1]) for x in range(8)]
        nodes_number = next(f).split()[-1]
        elements_number = next(f).split()[-1]
        next(f)
        nodes_data_string = [next(f).split(',') for x in range(int(nodes_number))]
        next(f)
        elements_data_string = [next(f).split(',') for x in range(int(elements_number))]
        next(f)
        BC_data = next(f).split(',')
        BC_data = [int(i) for i in BC_data]

    for i in range(int(nodes_number)):
        nodes_data.append(list(map(float, nodes_data_string[i])))
    for i in range(int(elements_number)):
        elements_data.append(list(map(int, elements_data_string[i])))

    file_data.append(global_data_values)
    file_data.append(nodes_data)
    file_data.append(elements_data)
    file_data.append(BC_data)
    return file_data


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

    def __str__(self):
        return f'ID = {self.ID} nodes ID = {self.nodes_ID}'


class Grid:
    def __init__(self, file_nodes_number, file_elements_number, nodes_data, elements_data, BC_data):
        self.nodes_number = file_nodes_number
        self.elements_number = file_elements_number
        self.nodes = []
        self.elements = []
        self.H = []
        for it, node in enumerate(nodes_data):
            node = Node(nodes_data[it][0], nodes_data[it][1], nodes_data[it][2])
            node.set_BC(node, BC_data)
            self.nodes.append(node)

        for it, element in enumerate(elements_data):
            self.elements.append(Element(elements_data[it][0], elements_data[it]))



    def show(self):
        print('Nodes info')
        for node in self.nodes:
            print(node)

        print('\nElements info')
        for element in self.elements:
            print(element)

        print('\nElements info')
        for H in self.H:
            print(H)


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


def f1(x):
    return (x * x) + (2 * x) + 1

def f2(x):
    return 0.5*x*x+2*x+3

HGlobal = []
def main():

    data = read_file('Test2_4_4_MixGrid.txt')
    global_data = GlobalData(data[0])
    #print(data[0])
    #print(data[1])
    print(data[2])
    #print(data[3])
    #print(global_data)
    grid = Grid(len(data[1]), len(data[2]), data[1], data[2], data[3])
    grid.show()

    npc = 2
    ele4 = Eleme4(npc)
    ele4_data = ele4.calculate()
   # ele4.draw()
    jakobian = Jakobian(ele4_data)
    inverted_jakobian = jakobian.calculate(npc)
    #jakobian.draw()

    for element in grid.elements:
        H = MatrixH(inverted_jakobian, ele4_data, jakobian.jakobs)
        H.calculate(npc)
        HGlobal.append(H.H)
    print("HGLOBAL")
    print(HGlobal)

   # matrixH = MatrixH(inverted_jakobian, ele4_data, jakobian.jakobs)
    #print(inverted_jakobian)
    #matrixH.calculate(npc)
   # agregate2D(grid, HGlobal)


main()
