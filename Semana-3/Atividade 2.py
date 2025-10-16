"""
atividade 2:
Implemente:e^x≈(1+ n/x​)^n com n crescente, e:

1-Explique por que, para x<0 e n muito grande, pode ocorrer cancelamento catastrófico;

2-Proponha um critério de parada numérico para encerrar o crescimento de 
n sem perder precisão.
"""
import math
import sys

def exp_limit(x, n0=10, n_max=10_000_000, growth=2.0, rtol=1e-14, atol=0.0):
    """
    Aproxima e^x por E_n(x) = (1 + x/n)^n, crescendo n até convergir.
    Usa log1p para estabilidade: E_n = exp(n * log1p(x/n)).
    """
    n = max(1, n0)
    prev = None
    while n <= n_max:
        y = math.exp(n * math.log1p(x / n))
        if prev is not None:
            if abs(y - prev) <= max(atol, rtol * abs(y)):
                return y, n
        prev = y
        n = int(max(n + 1, n * growth))
    return prev, n_max  # melhor aprox. dentro do limite


# Demonstração
def main ():
    print("\n--Atividade2--")
    for val in [1.0, 5.0, -2.0]:
        y, n = exp_limit(val)
        print(val, y, math.exp(val), n)

if __name__ == "__main__":
    main()

