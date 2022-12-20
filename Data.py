class Data():
    def __init__(self, filename):
        self.filename = filename
        self.global_data = []
        self.nodes_data = []
        self.elements_data = []
        self.BC_data = []
        self.read_grid_file()

    def read_grid_file(self):
        with open(self.filename, 'r') as f:
            self.global_data_values = [int(next(f).split()[-1]) for x in range(8)]
            nodes_number = next(f).split()[-1]
            elements_number = next(f).split()[-1]
            next(f)
            nodes_data_string = [next(f).split(',') for x in range(int(nodes_number))]
            next(f)
            elements_data_string = [next(f).split(',') for x in range(int(elements_number))]
            next(f)
            BC_data = next(f).split(',')
            self.BC_data = [int(i) for i in BC_data]

        for i in range(int(nodes_number)):
            self.nodes_data.append(list(map(float, nodes_data_string[i])))
        for i in range(int(elements_number)):
            self.elements_data.append(list(map(int, elements_data_string[i])))
