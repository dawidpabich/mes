class Element:
    def __init__(self, ID, nodes_ID):
        self.ID = ID
        self.nodes_ID = nodes_ID[1:5]
        self.H = None
        self.Hbc = None
        self.H_Final = None
        self.P = None
        self.C = None

    def __str__(self):
        return f'ID = {self.ID} nodes ID = {self.nodes_ID}'