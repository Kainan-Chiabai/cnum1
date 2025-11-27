import numpy as np
from algoritmos2 import (
    medio,
    trapezio,
    simpson,
    integral,
)

def f_atividade2(x):
    return np.exp(4 - x**2)

def integral_composta_n(metodo, f, a, b, N):
    
    if metodo == medio:

        M = N
        h = (b - a) / M
        
        s = 0.0
        for i in range(M):
            x_i = a + i * h
            s += h * f(x_i + h / 2)
        return s
    

    M = N - 1
    h = (b - a) / M
    
    if metodo == trapezio:

        s = f(a) + f(b)
        for i in range(1, M):
            x_i = a + i * h
            s += 2 * f(x_i)
        return s * h / 2
    
    elif metodo == simpson:

        if M % 2 != 0:
            print(f"Aviso: A regra de Simpson composta requer um número par de subintervalos. N={N} (M={M})")
            return 0.0
            
        s = f(a) + f(b)
        for i in range(1, M):
            x_i = a + i * h
            if i % 2 == 0:
                s += 2 * f(x_i)
            else:
                s += 4 * f(x_i)
        return s * h / 3
    
    else:
        return 0.0


def main():

    print("-- Atividade 2 (Tentativa de correção do Ponto Médio) --")

    a = 2
    b = 5
    
    N_values = [3, 5, 7, 9]
    
    results = {}
    
    for N in N_values:
        print(f"\n--- N = {N} pontos ---")
        

        r_medio = integral_composta_n(medio, f_atividade2, a, b, N)
        print(f"Ponto Médio = {r_medio:.7f}")
        
   
        r_trapezio = integral_composta_n(trapezio, f_atividade2, a, b, N)
        print(f"Trapézio = {r_trapezio:.7f}")
        
 
        r_simpson = integral_composta_n(simpson, f_atividade2, a, b, N)
        print(f"Simpson = {r_simpson:.7f}")
        
        results[N] = {
            "Ponto Médio": f"{r_medio:.7f}",
            "Trapézio": f"{r_trapezio:.7f}",
            "Simpson": f"{r_simpson:.7f}",
        }
        
    print("\n--- Tabela de Resultados ---")
    print("| n | Ponto Médio | Trapézio | Simpson |")
    print("|---|---|---|---|")
    
    for N in N_values:
        print(f"| {N} | {results[N]['Ponto Médio']} | {results[N]['Trapézio']} | {results[N]['Simpson']} |")


if __name__ == "__main__":
    main()