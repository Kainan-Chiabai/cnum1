import numpy as np

# Funções de quadratura simples
def medio(f, a, b):
    """Regra do Ponto Médio simples."""
    h = b - a
    return h * f((a + b) / 2)

def trapezio(f, a, b):
    """Regra do Trapézio simples."""
    h = b - a
    return h * (0.5 * f(a) + 0.5 * f(b))

def simpson(f, a, b):
    """Regra de Simpson simples."""
    h = (b - a) / 2
    return h * ((1 / 3) * f(a) + (4 / 3) * f((a + b) / 2) + (1 / 3) * f(b))

def integral(metodo, f, a, b, n=1e-3):
    """
    Função de integral composta que usa um método simples.
    'n' aqui representa o tamanho do subintervalo (h).
    """
    s = 0.0
    c = a
    d = a + n
    
    # Ajuste para garantir que o último intervalo chegue exatamente em 'b'
    while d <= b + 1e-9: # Adiciona uma pequena tolerância para flutuantes
        s += metodo(f, c, d)
        c = d
        d += n
        
    # Se o último 'd' ultrapassou 'b' (o que não deve acontecer com o loop acima), 
    # ou se 'b' não foi alcançado exatamente, o loop acima deve ser suficiente.
    # O código original do site usa 'n' como o tamanho do passo, o que é o que estou fazendo.
    
    return s

# Funções de quadratura composta (para Atividade 2)
def composta_medio(f, a, b, N):
    """Regra do Ponto Médio Composta com N subintervalos."""
    h = (b - a) / N
    soma = 0.0
    for i in range(N):
        x_i = a + i * h
        x_i_mais_1 = a + (i + 1) * h
        soma += f((x_i + x_i_mais_1) / 2)
    return h * soma

def composta_trapezio(f, a, b, N):
    """Regra do Trapézio Composta com N subintervalos."""
    h = (b - a) / N
    soma = 0.5 * (f(a) + f(b))
    for i in range(1, N):
        soma += f(a + i * h)
    return h * soma

def composta_simpson(f, a, b, N):
    """Regra de Simpson Composta com N subintervalos. N deve ser par."""
    if N % 2 != 0:
        raise ValueError("N deve ser par para a Regra de Simpson Composta.")
    h = (b - a) / N
    soma = f(a) + f(b)
    
    for i in range(1, N, 2):
        soma += 4 * f(a + i * h)
    
    for i in range(2, N - 1, 2):
        soma += 2 * f(a + i * h)
        
    return (h / 3) * soma