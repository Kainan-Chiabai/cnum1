import numpy as np
import matplotlib.pyplot as plt

from algoritmos import regressao


def plot(x, y, v, num_img=1):
    x_vals = np.linspace(min(x) - 0.25, max(x) + 0.25, 400)
    y_vals = np.zeros_like(x_vals, dtype=float)
    A = regressao(x, y, v)
    for p, ap in enumerate(A):
        y_vals += ap * (x_vals**p)
    plt.figure(figsize=(7, 4))
    plt.scatter(x, y, color="blue", label="Pontos dados")
    plt.plot(x_vals, y_vals, color="red", label="Ajuste linear f(x)")
    plt.title("Ajuste linear por mínimos quadrados")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle=":")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"semana-10/regressao_{num_img}.png", dpi=120, bbox_inches="tight")
    plt.close()


def main():
  
    print("-- Atividade 1 --")

    x = np.array([-0.35, 0.15, 0.23, 0.35], dtype=float)
    y = np.array([0.20, -0.50, 0.54, 0.70], dtype=float)
    v = lambda x: np.column_stack((np.ones(len(x)), x))

    A = regressao(x, y, v)

    print(A)
    plot(x, y, v, 1)

    print("-- Atividade 2 --")
    # Pontos dados na Atividade 2
    x = np.array([-1.94, -1.44, 0.93, 1.39], dtype=float)
    y = np.array([1.02, 0.59, -0.28, -1.04], dtype=float)
    
    # Função de base para f(x) = a1 + a2*x
    # A matriz V terá colunas [1, x]
    v = lambda x: np.column_stack((np.ones(len(x)), x))

    # Calcular os coeficientes A = [a1, a2]
    A = regressao(x, y, v)

    if A is not None:
        a1 = A[0] # Intercepto
        a2 = A[1] # Inclinação
        
        print(f"Coeficientes encontrados: A = [a1, a2] = {A}")
        print(f"Função ajustada: f(x) = {a1:.8f} + ({a2:.8f})x")
        
        # Calcular f(1)
        f_1 = a1 + a2 * 1
        print(f"Valor de f(1): {f_1:.7f}")

        # Gerar o gráfico
        plot(x, y, v, 2)

    print("-- Atividade 3 --")

    # Pontos dados na Atividade 3
    x = np.array([0.01, 1.02, 2.04, 2.95, 3.55], dtype=float)
    y = np.array([1.99, 4.55, 7.20, 9.51, 10.82], dtype=float)
    
    # Função de base para f(x) = c + b*x + a*x^2
    # A matriz V terá colunas [1, x, x^2]
    v = lambda x: np.column_stack((np.ones(len(x)), x, x**2))

    # Calcular os coeficientes A = [c, b, a]
    A = regressao(x, y, v)

    if A is not None:
        c = A[0] # Coeficiente linear (a1)
        b = A[1] # Coeficiente de x (a2)
        a = A[2] # Coeficiente de x^2 (a3)
        
        print(f"Coeficientes encontrados (c, b, a): {A}")
        
        # Formatando para a resposta esperada: y = ax^2 + bx + c
        print(f"Parábola ajustada: y = {a:.7f}x^2 + {b:.7f}x + {c:.7f}")

        # Gerar o gráfico
        plot(x, y, v, 3)   
if __name__ == "__main__":
    main()

