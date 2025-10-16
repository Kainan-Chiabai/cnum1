"""
Faça na linguagem Python uma função que calcula o fatorial de um número.
O fatorial de um número é o produto do número por todos os antecessores positivos.
"""
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("O número deve ser não negativo.")

    result = 1
    i = n
    
    while i > 1:
        result *= i
        i -= 1

    return result


    return result
def main():
    assert is_perfect(6) == True
    assert is_perfect(7) == False
    assert is_perfect(-1) == False
    assert factorial(5) == 120
    assert factorial(0) == 1
    try:
        factorial(-1)
    except ValueError as error:
        assert str(error) == "O número deve ser não negativo."

