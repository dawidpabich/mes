import numpy as np


def solveTemp(nodes_number, H_agr, P_agr, C_agr, initial_temp, simulation_time, simulation_step_time):
    time = 0
    t0 = np.full((nodes_number, 1), initial_temp)

    for i in range(simulation_time // simulation_step_time):
        time += simulation_step_time
        H_plus_C_przez_dT_razy_t0 = H_agr + C_agr / simulation_step_time

        C_przez_dT_razy_t0_plus_P = np.matmul(C_agr / simulation_step_time, t0) + P_agr

        t1 = np.linalg.solve(H_plus_C_przez_dT_razy_t0, C_przez_dT_razy_t0_plus_P)
        min = np.min(t1)
        max = np.max(t1)
        t0 = t1
        print(f"Time: {time}    min = {min}     max = {max}")

        # print("Iteracja: ", i)
        # print(f"Macierz H + C/dT")
        # for x in H_plus_C_przez_dT_razy_t0:
        #     print(x)
        #
        # print()
        # print(f"Wektor P + (C / dT) * T0")
        # for x in C_przez_dT_razy_t0_plus_P:
        #     print(x)
        # print()
