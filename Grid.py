from Node import Node
from Element import Element
from Data import Data

class Grid:
    def __init__(self, filename):
        self.data = Data(filename)
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