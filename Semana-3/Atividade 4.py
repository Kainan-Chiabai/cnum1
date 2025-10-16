import math
import sys
from decimal import Decimal, getcontext


def cos_series(x, rtol=1e-15, atol=0.0):
    """
    cos(x) pela série de Maclaurin com atualização recursiva do termo.
    Para quando |termo| < max(atol, rtol*|soma|, eps).
    """
    eps = sys.float_info.epsilon
    s = 1.0  # n=0
    term = 1.0
    n = 0
    while True:
        # atualiza para o próximo termo (2n -> 2(n+1))
        term *= -(x * x) / ((2 * n + 1) * (2 * n + 2))
        s_new = s + term
        if abs(term) < max(atol, rtol * abs(s_new), eps):
            s = s_new
            break
        s = s_new
        n += 1
        if n > 10_000:  # segurança
            break
    return s, n

def main():
    
    # Atividade 4
    print("-- Atividade 4 --")
    xs = [-20 + 40 * i / 199 for i in range(200)]
    errs = [abs(cos_series(x)[0] - math.cos(x)) for x in xs]
    print(f"xs={xs[:10]}\nerrs={errs[:10]}...")

if __name__ == "__main__":
    main()


