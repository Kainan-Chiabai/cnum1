import numpy as np

def main():
    # Atividade 1
    print("-- Atividade 1 --")
    A = np.array([
        [1, 1,  1],
        [4, 4,  2],
        [2, 1, -1]
    ], dtype=float)
    B = np.array([1, 2, 0], dtype=float)
    print("Matriz A:")
    print(A)
    print("\nVetor B:")
    print(B)
    print("\nSolução NumPy x:")
    X = np.linalg.solve(A, B)
    print(X)

if __name__ == "__main__":
    main()