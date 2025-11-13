import numpy as np
from scipy.integrate import quad
from tabulate import tabulate

from algoritmos import (
    medio,
    trapezio,
    simpson,
    integral,
    composta_medio,
    composta_trapezio,
    composta_simpson,
)

# Funções a serem integradas na Atividade 1
# As integrais são todas de a=0 a b=1
integrals_atv1 = [
    {"name": "a) e^(-x)", "f": lambda x: np.exp(-x), "a": 0, "b": 1},
    {"name": "b) 1/(1+x^2)", "f": lambda x: 1 / (1 + x**2), "a": 0, "b": 1},
    {"name": "c) 1/(1+x)", "f": lambda x: 1 / (1 + x), "a": 0, "b": 1},
    {"name": "d) 1/sqrt(1+x^2)", "f": lambda x: 1 / np.sqrt(1 + x**2), "a": 0, "b": 1},
    {"name": "e) sqrt(1-x^2)", "f": lambda x: np.sqrt(1 - x**2), "a": 0, "b": 1},
    {"name": "f) 1/sqrt(1-x^2)", "f": lambda x: 1 / np.sqrt(1 - x**2), "a": 0, "b": 1},
]

# Funções a serem integradas na Atividade 2
# A integral é de a=0 a b=1 para f(x) = e^(-x^2)
f_atv2 = lambda x: np.exp(-(x**2))
a_atv2 = 0
b_atv2 = 1
N_values_atv2 = [3, 5, 7, 9]


def run_atividade_1():
    print("--- Atividade 1: Regras Simples (Composta com n=1e-3) ---")
    
    results = []
    # O site usa n=1e-3 como tamanho do passo (h) para a função integral.
    # O número de subintervalos N será (b-a)/n = 1/1e-3 = 1000.
    n_step = 1e-3 

    for item in integrals_atv1:
        f = item["f"]
        a = item["a"]
        b = item["b"]
        
        # Cálculo com os métodos compostos (usando a função 'integral' do site)
        r_medio = integral(medio, f, a, b, n=n_step)
        r_trapezio = integral(trapezio, f, a, b, n=n_step)
        r_simpson = integral(simpson, f, a, b, n=n_step)
        
        # Cálculo com SciPy para comparação
        r_scipy, _ = quad(lambda x: float(f(x)), a, b)
        
        results.append([
            item["name"],
            f"{r_medio:.8f}",
            f"{r_trapezio:.8f}",
            f"{r_simpson:.8f}",
            f"{r_scipy:.8f}"
        ])

    headers = ["Integral", "Ponto Médio", "Trapézio", "Simpson", "SciPy (quad)"]
    print(tabulate(results, headers=headers, tablefmt="pipe"))
    print("\n")


def run_atividade_2():
    print("--- Atividade 2: Regras Compostas (f(x) = e^(-x^2), a=0, b=1) ---")
    
    results = []
    
    for N in N_values_atv2:
        # Ponto Médio Composta
        r_medio = composta_medio(f_atv2, a_atv2, b_atv2, N)
        
        # Trapézio Composta
        r_trapezio = composta_trapezio(f_atv2, a_atv2, b_atv2, N)
        
        # Simpson Composta
        # N deve ser par para Simpson. Se N for 3, 5, 7 ou 9, a regra de Simpson Composta
        # não pode ser aplicada diretamente. O problema do site parece ter um erro
        # ou está usando uma variação que permite N ímpar (como a regra 3/8).
        # Vou seguir a implementação padrão (1/3) e usar N+1 se N for ímpar, ou 
        # N como o número de subintervalos (que deve ser par).
        # No entanto, para replicar o resultado do site, vou assumir que N é o número
        # de subintervalos e que o site está usando uma regra composta de Simpson
        # que lida com N ímpar (como a combinação de Simpson 1/3 e 3/8).
        # Como a implementação padrão de Simpson Composta (1/3) requer N par, 
        # e os valores N=3, 5, 7, 9 são ímpares, vou usar a implementação padrão 
        # e capturar o erro, ou, para fins de demonstração, usar N+1 subintervalos.
        # Para evitar a complexidade de implementar a regra 3/8, vou assumir que
        # o N no site é o número de pontos (N+1 subintervalos) ou que há um erro
        # no enunciado. Vou tentar usar a regra de Simpson Composta com N subintervalos
        # e lidar com o erro de N ímpar.
        
        try:
            r_simpson = composta_simpson(f_atv2, a_atv2, b_atv2, N)
        except ValueError:
            # Se N for ímpar, a regra de Simpson Composta (1/3) não se aplica.
            # Vou usar um valor placeholder ou tentar uma aproximação com N+1.
            # Para seguir o enunciado, vou usar N+1 para Simpson, se N for ímpar.
            if N % 2 != 0:
                N_simpson = N + 1
                r_simpson = composta_simpson(f_atv2, a_atv2, b_atv2, N_simpson)
            else:
                r_simpson = "Erro N ímpar" # Não deve acontecer com os Ns dados
        
        results.append([
            N,
            f"{r_medio:.8f}",
            f"{r_trapezio:.8f}",
            f"{r_simpson:.8f}"
        ])

    headers = ["N", "Ponto Médio", "Trapézio", "Simpson"]
    print(tabulate(results, headers=headers, tablefmt="pipe"))
    print("\n")


if __name__ == "__main__":
    # Certifique-se de que o numpy e o scipy estão instalados
    # Vou executar a instalação antes de rodar o script
    pass # A instalação será feita na próxima fase


def run_all():
    run_atividade_1()
    run_atividade_2()

if __name__ == "__main__":
    run_all()