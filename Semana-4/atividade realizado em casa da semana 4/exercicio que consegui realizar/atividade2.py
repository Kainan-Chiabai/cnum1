import numpy as np
import matplotlib.pyplot as plt
from algoritmos import bissecao

# =====================
# Definições das funções
# =====================
def f1(x):
    return x**3 - x - 2

def f2(x):
    return x - np.cos(x)

# =====================
# Função para plotar
# =====================
def plot(f, number=1):
    x_vals = np.arange(-2, 3, 0.01)
    y_vals = f(x_vals)

    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.plot(x_vals, y_vals, label="f(x)")
    plt.grid(True)
    plt.title(f"Função {number}")
    plt.legend()

    plt.savefig(f"bissecao_{number}.png", dpi=120, bbox_inches="tight")
    plt.close()


def main():
    # -------- Atividade 2 --------
    print("\n-- Atividade 2 --")
    plot(f2, 2)
    r, i = bissecao(f2, 0, 1, 1e-4, iter=4)
    print(f"Raiz aproximada de f2 = {r}, em {i} iterações")

if __name__ == "__main__":
    main()