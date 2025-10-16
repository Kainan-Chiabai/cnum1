import numpy as np

from algoritmos import (
    G,
    GN,
    fixed_point,
)


def main():
    print("-- Atividade 3 --")

    def F(x):
        x1, x2 = x
        return np.array([
            (1.0/8.0)*(x1**2) + (1.0/5.0)*((x2 - 1.0)**2) - 1.0,
            np.arctan(x1) + x1 - x2 - (x2**3)
        ], dtype=float)

    def J(x):
        x1, x2 = x
        return np.array([
            [x1/4.0,           (1.0/5.0)*(2.0*x2 - 2.0)],
            [((x1**2) + 2.0)/((x1**2) + 1.0),   -(3.0*(x2**2)) - 1.0]
        ], dtype=float)
    
    x = np.array([-1.0, -1.0], dtype=float)
    r = fixed_point(x, lambda x: G(x, F, J))
    print(r)
    r = fixed_point(x, lambda x: GN(x, F))
    print(r)

    x = np.array([3.0, 1.0], dtype=float)
    r = fixed_point(x, lambda x: G(x, F, J))
    print(r)
    r = fixed_point(x, lambda x: GN(x, F))
    print(r)
    
if __name__ == "__main__":
    main()