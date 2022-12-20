import numpy as np


def agregateH(grid):
    size = len(grid.nodes)
    H_aggregated_matrix = np.zeros((size, size))
    for element in grid.elements:
        for i in range(4):
            for j in range(4):
                H_aggregated_matrix[element.nodes_ID[i] - 1][element.nodes_ID[j] - 1] += element.H[i][j]
    return H_aggregated_matrix


def agregateP(grid):
    size = len(grid.nodes)
    P_aggregated_matrix = np.zeros((size, 1))
    for element in grid.elements:
        for i in range(4):
            P_aggregated_matrix[element.nodes_ID[i] - 1] += element.P[i]
    return P_aggregated_matrix

def agregateC(grid):
    size = len(grid.nodes)
    C_aggregated_matrix = np.zeros((size, size))
    for element in grid.elements:
        for i in range(4):
            for j in range(4):
                C_aggregated_matrix[element.nodes_ID[i] - 1][element.nodes_ID[j] - 1] += element.C[i][j]
    return C_aggregated_matrix
