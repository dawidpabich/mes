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