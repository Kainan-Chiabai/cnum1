import numpy as np
from algoritmos import lu

def solve_circuit(V, R1, R2, R3, R4, R5, R6, R7, R8):

    # Matriz A
    A = np.array([
        [-(1/R1 + 1/R2 + 1/R5), 1/R2, 0, 0],
        [1/R2, -(1/R2 + 1/R3 + 1/R6), 1/R3, 0],
        [0, 1/R3, -(1/R3 + 1/R4 + 1/R7), 1/R4],
        [0, 0, 1/R4, -(1/R4 + 1/R8)]
    ])

    # Vetor B
    B = np.array([-V/R1, 0, 0, 0])

   
    X = lu(A, B)
    return X

def main():
    V = 127

    # Caso a
    R_a = {'R1': 2, 'R2': 2, 'R3': 2, 'R4': 2, 'R5': 100, 'R6': 100, 'R7': 100, 'R8': 50}
    V_a = solve_circuit(V, **R_a)
    print("--- Caso a ---")
    print(f"V1 = {V:.4g} V")
    print(f"V2 = {V_a[0]:.4g} V")
    print(f"V3 = {V_a[1]:.4g} V")
    print(f"V4 = {V_a[2]:.4g} V")
    print(f"V5 = {V_a[3]:.4g} V")
    print("\n")

    # Caso b
    R_b = {'R1': 2, 'R2': 2, 'R3': 2, 'R4': 2, 'R5': 50, 'R6': 100, 'R7': 100, 'R8': 100}
    V_b = solve_circuit(V, **R_b)
    print("--- Caso b ---")
    print(f"V1 = {V:.4g} V")
    print(f"V2 = {V_b[0]:.4g} V")
    print(f"V3 = {V_b[1]:.4g} V")
    print(f"V4 = {V_b[2]:.4g} V")
    print(f"V5 = {V_b[3]:.4g} V")

if __name__ == "__main__":
    main()

# revisar o conceito da questão para resolver a questão colocando a criação da matriz 