import math
import sys
from decimal import Decimal, getcontext

def min_terms_for_tol(x, tol=1e-12):
    term = 1.0
    n = 0
    while term > tol:
        n += 1
        term *= abs(x) / n
        if n > 100_000:
            break
    return n

def main():
  
    print("-- Atividade 5 --")
    for x in [1, 3, 10]:
        n = min_terms_for_tol(x, 1e-12)
        print(f"x={x}: ~{n} termos para atingir tol=1e-12")
   
if __name__ == "__main__":
    main()    
