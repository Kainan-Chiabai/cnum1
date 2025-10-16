"""
Faça na linguagem Python uma função que verifica se um número é primo.
Um número que só pode ser dividido por um e por ele mesmo.
"""
import numpy as np
import matplotlib.pyplot as plt

def is_perfect(n: int) -> bool:
    if n < 1:
        return False

    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i

    return sum_divisors == n

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("O número deve ser não negativo.")

    result = 1
    i = n
    while i > 1:
        result *= i
        i -= 1

    return result

def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n/2)):
        if n % i == 0:
            return False

    return True

if __name__ == "__main__":
    main()