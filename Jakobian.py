class Jakobian():
    def __init__(self, ele4_data, nodes_ID, nodes, npc):
        self.ele4_data = ele4_data
        self.ksi_data = ele4_data[0]
        self.eta_data = ele4_data[1]
        self.nodes_ID = nodes_ID
        self.nodes = nodes
        self.jakobs = []
        self.inv_jakob = []
        self.x = []
        self.y = []

        for i in range(4):
            self.x.append(self.nodes[self.nodes_ID[i] - 1].x)
            self.y.append(self.nodes[self.nodes_ID[i] - 1].y)

        self.calculate(npc)

    def calculate(self, npc):

        jakob = [[0, 0], [0, 0]]
        inv_jakob = [[0, 0], [0, 0]]
        detJ = 0
        for j in range(npc ** 2):
            # dx po dksi
            jakob[0][0] = self.ksi_data[j][0] * self.x[0] + self.ksi_data[j][1] * self.x[1] + self.ksi_data[j][2] * \
                          self.x[2] + self.ksi_data[j][3] * self.x[3]
            # dy po dksi
            jakob[0][1] = self.ksi_data[j][0] * self.y[0] + self.ksi_data[j][1] * self.y[1] + self.ksi_data[j][2] * \
                          self.y[2] + self.ksi_data[j][3] * self.y[3]
            # dx po deta
            jakob[1][0] = self.eta_data[j][0] * self.x[0] + self.eta_data[j][1] * self.x[1] + self.eta_data[j][2] * \
                          self.x[2] + self.eta_data[j][3] * self.x[3]
            # dy po deta
            jakob[1][1] = self.eta_data[j][0] * self.y[0] + self.eta_data[j][1] * self.y[1] + self.eta_data[j][2] * \
                          self.y[2] + self.eta_data[j][3] * self.y[3]

            detJ = jakob[0][0] * jakob[1][1] - (jakob[1][0] * jakob[0][1])
            self.jakobs.append(detJ)
            print("jakob")
            for x in jakob:
                print(x)

            # # dy po deta
            # inv_jakob[0][0] = 1 / detJ * jakob[1][1]
            # # -dy po dksi
            # inv_jakob[0][1] = -1 / detJ * jakob[0][1]
            # # -dx po deta
            # inv_jakob[1][0] = -1 / detJ * jakob[1][0]
            # # dx po dksi
            # inv_jakob[1][1] = 1 / detJ * jakob[0][0]
            # dy po deta
            inv_jakob[0][0] = jakob[0][0]
            # -dy po dksi
            inv_jakob[0][1] = jakob[0][1]
            # -dx po deta
            inv_jakob[1][0] = jakob[1][0]
            # dx po dksi
            inv_jakob[1][1] = jakob[1][1]
            self.inv_jakob.append(inv_jakob)

    def draw(self):
        print("Jakobian: ")
        for list in self.jakobs:
            for x in list:
                print(x, end=" ")
            print()
