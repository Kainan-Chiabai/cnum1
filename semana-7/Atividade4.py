import numpy as np

from algoritmos import (
    G,
    GN,
    fixed_point,
)


def main():
 
    print("-- Atividade 4 --")

    def F(x):
        x1, x2, x3, k = x
        return np.array([
            x1 + x2 + x3 - 1500.0,
            (0.3 + 2e-4*x1 + 4*3.4e-9*(x1**3)) - k,
            (0.25 + 4e-4*x2 + 3*4.3e-7*(x2**2)) - k,
            (0.19 + 2*5e-4*x3 + 4*1.1e-7*(x3**3)) - k
        ], dtype=float)

    def J(x):
        x1, x2, x3, k = x
        return np.array([
            [1.0, 1.0, 1.0, 0.0],
            [2e-4 + 3*4*3.4e-9*(x1**2), 0.0, 0.0, -1.0],
            [0.0, 4e-4 + 2*3*4.3e-7*(x2), 0.0, -1.0],
            [0.0, 0.0, 2*5e-4 + 3*4*1.1e-7*(x3**2), -1.0]
        ], dtype=float)
    
    x = np.array([500.0, 500.0, 500.0, 1.0], dtype=float)
    r = fixed_point(x, lambda x: G(x, F, J))
    print(r)
    r = fixed_point(x, lambda x: GN(x, F))
    print(r)

if __name__ == "__main__":
    main()