"""
Faça na linguagem Python uma função que verifica se um número é perfeito.Um número é perfeito se a soma dos divisores for igual a ele mesmo (ex: 6 = 1 + 2 + 3).
A partir de agora, vamos usar um ambiente virtual para execução dos nossos códigos.Em Python, venv é um módulo que permite criar ambientes virtuais isolados, 
fundamentais para manter as dependências de cada projeto separadas e evitar conflitos com outras aplicações:
"""
def is_perfect(n: int) -> bool:
    if n < 1:
        return False

    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i

    return sum_divisors == n


def main():
    assert is_perfect(6) == True
    assert is_perfect(7) == False
    assert is_perfect(-1) == False


if __name__ == "__main__":
    main()