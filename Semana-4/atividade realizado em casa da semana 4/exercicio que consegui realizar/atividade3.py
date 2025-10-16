import numpy as np
import matplotlib.pyplot as plt
from algoritmos import bissecao

# =====================
# Definição da função da Atividade 3
# =====================
def f3(x):
    return 5*np.sin(x**2) - np.exp(x/10)

# =====================
# Função para plotar
# =====================
def plot_f3():
    x_vals = np.arange(0, 3, 0.01)
    y_vals = f3(x_vals)

    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.plot(x_vals, y_vals, label="f(x) = 5sin(x²) - exp(x/10)")
    plt.grid(True)
    plt.title("Função da Atividade 3")
    plt.legend()

    plt.savefig("bissecao_atividade3.png", dpi=120, bbox_inches="tight")
    plt.close()

# =====================
# Programa principal
# =====================
def main():
    print("-- Atividade 3 --")
    plot_f3()

    # Intervalos observados no gráfico
    intervalos = [(0.4, 0.5), (1.7, 1.8), (2.5, 2.6)]
    for a, b in intervalos:
        r, i = bissecao(f3, a, b, 1e-5, iter=50)
        print(f"Intervalo ({a}, {b}) -> raiz ≈ {r:.5f}, obtida em {i} iterações")

if __name__ == "__main__":
    main()