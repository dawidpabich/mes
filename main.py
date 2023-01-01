from GlobalData import GlobalData
from Grid import Grid
from Element4 import Element4
from Jakobian import Jakobian
from MatrixH import MatrixH
from Agregate import *
from MatrixHBC import MatrixHBC
from Element4HBC import Element4HBC
from VectorP import VectorP
from MatrixC import MatrixC
from Simulation import simulation


def main():
    np.set_printoptions(linewidth=300)
    grid = Grid("Test2_4_4_MixGrid.txt")
    global_data = GlobalData(grid.data.global_data_values)

    npc = 3
    element4 = Element4(npc)
    # element4.calculate()
    element4_data = element4.calculate()

    element4HBC = Element4HBC(npc, global_data.Alfa)
    element4HBC.calculate()

    for it, element in enumerate(grid.elements):
        print(f"ELEMENT {it}")
        jakob = Jakobian(element4_data, element.nodes_ID, grid.nodes, npc)

        matrixH = MatrixH(jakob.inv_jakob, element4_data, global_data.Conductivity, jakob.jakobs, npc)
        element.H = matrixH.H
        print(f"element.HLocal:\n {element.H}")

        # matrixHBC = MatrixHBC(element, grid.nodes, element4HBC, global_data.Alfa)
        # element.Hbc = matrixHBC.HBC
        # print(f"element.HBC:\n {element.Hbc}")
        #
        # matrixP = VectorP(element, grid.nodes, element4HBC, 300, 1200, 2)
        # element.P = matrixP.P
        # print(f"element.P:\n {element.P}")
        #
        # element.H += element.Hbc
        # #print(element.H)
        #
        # matrixC = MatrixC(element4, jakob.jakobs, global_data.Density, global_data.SpecificHeat, npc)
        # element.C = matrixC.C
        # element.H += element.C
        # print(element.H/50)
        # print(f"element.C:\n {element.C}")
    #
    # H_aggregated = agregateH(grid)
    # P_aggregated = agregateP(grid)
    # C_aggregated = agregateC(grid)

    # print("H_Final aggregated:")
    # for x in H_aggregated:
    #    print(x)
    # print("P aggregated:")
    # for x in P_aggregated:
    #     print(x)
    # print("C aggregated")
    # for x in C_aggregated:
    #     print(x, end='\n')

    # print()
    # simulation(len(grid.nodes), H_aggregated, P_aggregated, C_aggregated, global_data.InitialTemp,
    #            global_data.SimulationTime, global_data.SimulationStepTime)


main()

# grid = Grid()
# element4HBC = Element4HBC(2, 300)
# element4HBC.calculate()
# matrixP = VectorP(grid.elements[0], grid.nodes, element4HBC, 25, 1200, 2)
