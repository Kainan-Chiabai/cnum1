import numpy as np
from algoritmos import (
    lu,
    jacobi,
    seidel,
)

# Atividade 3
# Faça uma permutação de linhas no sistema abaixo e resolva pelos métodos de Jacobi e Gauss-Seidel:
# x1 + 10x2 + 3x3 = 27
# 4x1 + 0x2 + x3 = 6
# 2x1 + x2 + 4x3 = 12

def main():
    print("\n-- Atividade 3 --")
    A = np.array([[4, 0, 1], [1, 10, 3], [2, 1, 4]], dtype=float)
    B = np.array([6, 27, 12], dtype=float)
    
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
