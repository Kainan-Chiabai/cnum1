"""
Instale e importe a biblioteca NumPy,que é fundamental para computação científica em Python,
oferecendo suporte para arrays e matrizes multidimensionais, além de uma vasta coleção de funções matemáticas de alto nível para operar eficientemente. 
Para instalar, utilize o comando:

pip install numpy

Escreva um algoritmo que realize o seguinte produto matricial:

[ [1, 2, 3],
[4, 5, 6],
[7, 8, 9] ]

multiplicado por:

[ [11, 12, 13],
[14, 15, 16],
[17, 18, 19] ]
"""
import numpy as np


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

def sum_of_digits(n: int) -> int:
    if n < 0:
        raise ValueError("O número deve ser não negativo.")
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[10, 11, 12],
              [13, 14, 15],
              [16, 17, 18]])

C = A @ B



if __name__ == "__main__":
    main()