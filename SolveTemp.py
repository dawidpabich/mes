import numpy as np

def solveTemp(H_agr, P_agr, C_agr, initial_temp, simulation_time, simulation_step_time):
    dT = 0

    t0 = np.full((16, 1), initial_temp)
    t1 = np.full((16, 1), 1)

    H_plus_C_przez_dT_razy_t0 = H_agr + C_agr / simulation_step_time

    C_przez_dT_razy_t0_plus_P = np.matmul(C_agr / simulation_step_time, t0) + P_agr

    t1 = np.linalg.solve(H_plus_C_przez_dT_razy_t0, C_przez_dT_razy_t0_plus_P)



    print("Macierz H + C/dT")
    for x in H_plus_C_przez_dT_razy_t0:
        print(x)

    print()
    print("Wektor P + (C / dT) * T0")
    for x in C_przez_dT_razy_t0_plus_P:
        print(x)

    print()
    min = np.min(t1)
    max = np.max(t1)
    print(min, max)
    print()
    print(t1)
