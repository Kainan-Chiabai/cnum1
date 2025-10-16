#atividade 3
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

def exp_series_scaling(x, theta=1.0):
    if x==0.0:
        return 1.0,0.0,0
    k=max(0,math.ceil(math.log2(abs(x)/theta))) if abs(x)>theta else 0
    m = x/ (2**k)

    em,n_terms,_ = exp_series(m)
    y = em
    for _ in range(k):
        y*=y
    
    return y,k,n_terms

def main ():
    
    print("\n--Atividade3--")
    
    for val in [10.0, -20.0]:
        y, k, n = exp_series_scaling(val, theta=1.0)
        print(f"x={val:+g} -> e^x ≈ {y:.6e} (math.exp={math.exp(val):.6e})  [k={k}, termos série(m)={n}]")

if __name__ == "__main__":
    main()




