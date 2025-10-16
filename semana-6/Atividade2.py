import numpy as np

from algoritmos import (
    lu,
    jacobi,
    seidel,
)
"""
Sistema de equações:

5x1 + x2  + x3  = 50
-x1 + 3x2 + x3  = 10
x1  + 2x2 + 10x3  =-30
"""

def main():

    # Atividade 2
    print("\n-- Atividade 2 --")

    #Coeficientes da matriz
    A = np.array([[5, 1, 1], [-1, 3, -1], [1, 2, 10]], dtype=float)
    B = np.array([50, 10, -30], dtype=float)
    print("\nMatriz A:")
    print(A)
    print("\nVetor B:")
    print(B)
    print("\nSolução Jacobi x:")
    X = jacobi(A, B, 100, 1e-8)
    print(X)
    print("\nSolução Seidel x:")
    X = seidel(A, B, 100, 1e-8)
    print(X)
    print("\nSolução LU x:")
    X = lu(A, B)
    print(X)
    print("\nSolução NumPy x:")
    X = np.linalg.solve(A, B)
    print(X)
if __name__ == "__main__":
    main()