
import math
import algoritmos
from scipy import integrate

def main():

    fa = lambda x: math.exp(-x)
    fb = lambda x: x**2
    fc = lambda x: x**3
    fd = lambda x: x * math.exp(-(x**2))
    fe = lambda x: 1 / (x**2 + 1)
    ff = lambda x: x / (x**2 + 1)

    funcoes = {
        'a': fa,
        'b': fb,
        'c': fc,
        'd': fd,
        'e': fe,
        'f': ff
    }

    a = 0
    b = 1
    passo = 1e-3

    print(f"{'f':^5} | {'Ponto médio':^12} | {'Trapézio':^12} | {'Simpson':^12} | {'SciPy':^12}")
    print("-" * 65)

    for nome, f in funcoes.items():

        res_medio = algoritmos.integral(algoritmos.medio, f, a, b, n=passo)
        res_trapezio = algoritmos.integral(algoritmos.trapezio, f, a, b, n=passo)
        res_simpson = algoritmos.integral(algoritmos.simpson, f, a, b, n=passo)
        
        res_scipy, _ = integrate.quad(f, a, b)

        print(f"{nome:^5} | {res_medio:12.8f} | {res_trapezio:12.8f} | {res_simpson:12.8f} | {res_scipy:12.8f}")

if __name__ == "__main__":
    main()