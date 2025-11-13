import numpy as np
import matplotlib.pyplot as plt
from algoritmos import regressao

def plot_trig(x, y, A, num_img):
    """
    Plota o ajuste para o item (a): Trigonométrico
    f(x) = a + b*sin(2*pi*x) + c*cos(2*pi*x)
    """
    x_vals = np.linspace(min(x), max(x), 400)
    
    a, b, c = A[0], A[1], A[2]
    y_vals = a + b * np.sin(2 * np.pi * x_vals) + c * np.cos(2 * np.pi * x_vals)

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color="blue", label="Pontos dados")
    plt.plot(x_vals, y_vals, color="red", label=f"f(x) = {a:.2f} + {b:.2f}sin(2πx) + {c:.2f}cos(2πx)")
    plt.title(f"Atividade {num_img}: Ajuste Trigonométrico")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle=":")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"regressao_{num_img}.png", dpi=120, bbox_inches="tight")
    plt.close()
    print(f"Gráfico 'regressao_{num_img}.png' salvo.")

def plot_poly(x, y, A, num_img):
    """
    Plota o ajuste para o item (b): Polinomial Cúbico
    f(x) = a + bx + cx^2 + dx^3
    """
    x_vals = np.linspace(min(x) - 0.1, max(x) + 0.1, 400)
    
    # Avaliação genérica do polinômio
    y_vals = np.zeros_like(x_vals, dtype=float)
    for p, ap in enumerate(A):
        y_vals += ap * (x_vals**p)
    
    a, b, c, d = A[0], A[1], A[2], A[3]

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color="blue", label="Pontos dados")
    plt.plot(x_vals, y_vals, color="green", label=f"f(x) = {a:.2f} + {b:.2f}x + {c:.2f}x² + {d:.2f}x³")
    plt.title(f"Atividade {num_img}: Ajuste Polinomial Cúbico")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle=":")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"regressao_{num_img}.png", dpi=120, bbox_inches="tight")
    plt.close()
    print(f"Gráfico 'regressao_{num_img}.png' salvo.")


def main():
    # Dados da Atividade 4 (completos)
    x = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], dtype=float)
    y = np.array([31, 35, 37, 33, 28, 20, 16, 15, 18, 23, 31], dtype=float)

    # --- Atividade 4a ---
    print("\n-- Atividade 4a (Ajuste Trigonométrico) --")
    
    # f(x) = a + b*sin(2*pi*x) + c*cos(2*pi*x)
    # Base: [1, sin(2*pi*x), cos(2*pi*x)]
    v_a = lambda x_in: np.column_stack((
        np.ones(len(x_in)), 
        np.sin(2 * np.pi * x_in), 
        np.cos(2 * np.pi * x_in)
    ))
    
    # Coeficientes A = [a, b, c]
    A_a = regressao(x, y, v_a)
    
    if A_a is not None:
        print(f"Coeficientes encontrados (a, b, c):")
        print(f"a = {A_a[0]:.7f}")
        print(f"b = {A_a[1]:.7f}")
        print(f"c = {A_a[2]:.7f}")
        plot_trig(x, y, A_a, "4a")

    # --- Atividade 4b ---
    print("\n-- Atividade 4b (Ajuste Polinomial Cúbico) --")
    
    # f(x) = a + bx + cx^2 + dx^3
    # Base: [1, x, x^2, x^3]
    v_b = lambda x_in: np.column_stack((
        np.ones(len(x_in)), 
        x_in, 
        x_in**2, 
        x_in**3
    ))
    
    # Coeficientes A = [a, b, c, d]
    A_b = regressao(x, y, v_b)
    
    if A_b is not None:
        print(f"Coeficientes encontrados (a, b, c, d):")
        print(f"a = {A_b[0]:.7f}")
        print(f"b = {A_b[1]:.7f}")
        print(f"c = {A_b[2]:.7f}")
        print(f"d = {A_b[3]:.7f}")
        plot_poly(x, y, A_b, "4b")

if __name__ == "__main__":
    main()