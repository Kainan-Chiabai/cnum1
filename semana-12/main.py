import numpy as np
from scipy.integrate import quad

from algoritmos import (
    medio,
    trapezio,
    simpson,
    integral,
)


def main():
    # Atividade 1
    print("-- Atividade 1 --")

    a = 0
    b = 1

    print("f(x) = e^(-x)")
    f = lambda x: np.exp(-x)
    r = integral(medio, f, a, b)
    print(f"Ponto medio = {r:.8}")
    r = integral(trapezio, f, a, b)
    print(f"Trapezio = {r:.8}")
    r = integral(simpson, f, a, b)
    print(f"Simpson = {r:.8}")
    r, error = quad(lambda x: float(f(x)), a, b)
    print(f"SciPy = {r:.8}")


if __name__ == "__main__":
    main()
# ainda falta fazer para cada questão