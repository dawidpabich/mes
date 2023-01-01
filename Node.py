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