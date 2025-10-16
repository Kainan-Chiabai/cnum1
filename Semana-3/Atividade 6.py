import math
import sys
from decimal import Decimal, getcontext

def exp_decimal(x, prec=80):
    """
    e^x em alta precisão usando decimal:
    - converte x para Decimal
    - usa série de Maclaurin com parada por precisão do contexto
    """
    getcontext().prec = prec
    xd = Decimal(str(x))
    s = Decimal(1)
    term = Decimal(1)
    n = 0
    # tolerância ~ 10^{-(prec-2)}
    tol = Decimal(1) / (Decimal(10) ** (prec - 2))
    while True:
        n += 1
        term *= xd / n
        s_new = s + term
        if abs(term) < tol:
            s = s_new
            break
        s = s_new
        if n > 20_000:
            break
    return +s  # aplica arredondamento do contexto


def compare_float_vs_highprecision(xs=(20, 40, 50), prec=80):
    rows = []
    for x in xs:
        hp = exp_decimal(x, prec=prec)
        fp = (
            math.exp(x) if x < 709.78 else float("inf")
        )  # limiar de overflow do float64
        # erro relativo quando possível
        if math.isfinite(fp):
            rel = abs((Decimal(str(fp)) - hp) / hp)
            rel_str = f"{rel:.2E}"
        else:
            rel_str = "overflow(float64)"
        rows.append((x, str(hp), fp, rel_str))
    return rows


def main():
  
    # Atividade 6
    print("-- Atividade 6 --")
    for r in compare_float_vs_highprecision((20, 40, 50), prec=80):
        print(f"x={r[0]}  high-prec={r[1][:18]}...  float64={r[2]}  erro_rel={r[3]}")


if __name__ == "__main__":
    main()