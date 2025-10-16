"""
A função exponencial natural pode ser definida pelo limite: e^x=lim⁡n→∞(1+x/n)^n,mas também é dada pela série de Maclaurin.
Implemente em Python o cálculo de e^x pela série, interrompendo a soma quando o termo ficar menor que o limite prático de contribuição, usando a precisão de máquina como critério. 
"""
import math
import sys

def exp_series(x, atol=0.0):
    """ Aproxima e^x pela série de Maclaurin com critério de parada numérico. """
    eps = sys.float_info.epsilon
    s = 1.0
    term = 1.0
    n = 0
    tol_abs = max(atol, eps)

    while True:
        n += 1
        term *= x / n
        s += term
        if abs(term) < eps * abs(s) or abs(term) < tol_abs:
            break
        if n > 10_000:
            break
    return s, n, term

# Demonstração
def main ():
    print("\n--Atividade1--")
    for val in [1.0, 5.0, -2.0]:
        approx, nterms, last = exp_series(val)
        print(f"x={val:+g} -> e^x ≈ {approx:.16g} (math.exp={math.exp(val):.16g}, termos={nterms})")

if __name__ == "__main__":
    main()