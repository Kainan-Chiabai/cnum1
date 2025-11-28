
import numpy as np
from algoritmos import *

# Atividade 1
x1 = np.array([1.5, 2.0, 2.2, 3.0])
y1 = np.array([4.9, 3.3, 3.0, 2.0])
x_new1 = np.array([1.75, 2.5, 2.75, 3.2])

# Usando interpolação polinomial (Vandermonde)
coef1_vandermonde = polinomial(x1, y1)
y_new1_vandermonde = poly_val(coef1_vandermonde, x_new1)

# Usando interpolação de Lagrange para comparação
coef1_lagrange = lagrange(x1, y1)
y_new1_lagrange = poly_val(coef1_lagrange, x_new1)

print("Atividade 1:")
print(f"Temperaturas (Vandermonde): {np.round(y_new1_vandermonde, 2)}")
# Atividade 2
x2 = np.array([0.2, 0.5, 0.7, 1.0])
y2 = np.array([0.8187, 1.5815, 1.9354, 2.2905])
x_new2 = np.array([0.3, 0.9])

# Usando interpolação polinomial
coef2 = polinomial(x2, y2)
y_new2 = poly_val(coef2, x_new2)

print("\nAtividade 2:")
print(f"I(0.3) = {y_new2[0]:.6f} A")
print(f"I(0.9) = {y_new2[1]:.6f} A")

# Atividade 3
# Outono
x3_outono = np.array([1, 1.25, 1.5, 1.75, 2])
y3_outono = np.array([38, 40, 42, 44, 46])
coef3_outono = regressao(x3_outono, y3_outono, v_linear)

# Inverno
x3_inverno = np.array([1, 1.5, 2, 2.5, 3])
y3_inverno = np.array([40, 44, 48, 52, 56])
coef3_inverno = regressao(x3_inverno, y3_inverno, v_linear)

# Primavera
x3_primavera = np.array([1, 1.15, 1.3, 1.45, 1.6])
y3_primavera = np.array([36, 39, 42, 45, 48])
coef3_primavera = regressao(x3_primavera, y3_primavera, v_linear)

print("\nAtividade 3:")
print(f"Outono: a1 = {coef3_outono[0]:.0f}, a0 = {coef3_outono[1]:.0f} ")
print(f"Inverno: a1 = {coef3_inverno[0]:.0f}, a0 = {coef3_inverno[1]:.0f} ")
print(f"Primavera: a1 = {coef3_primavera[0]:.0f}, a0 = {coef3_primavera[1]:.0f} ")

# Atividade 4
x4 = np.array([0.5, 1.1, 1.5, 2.2, 2.5, 3.1])
y4 = np.array([5.1, 10.3, 15.2, 20.1, 24.7, 30.5])

# V = Req * I + b
coef4 = regressao(x4, y4, v_linear)
Req = coef4[0]
b = coef4[1]

print("\nAtividade 4:")
print(f"Req = {Req:.7f} Ohm")
print(f"b = {b:.7f} V")

# Atividade 5, 6, 7
R = 5
L = 0.1
t = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
I = np.array([0.00, 0.82, 1.36, 1.60, 1.73])
h = 0.1 

# --- Atividade 5: I(t) linear  ---
# Coeficientes: [a1, a0]
coef_I5 = regressao(t, I, v_linear)
def I_func5(t_val):
   
    return poly_val(coef_I5, t_val)

dIdt5 = coef_I5[0] 
V_0_5_5 = L * dIdt5 + R * I_func5(0.5)

print("\nAtividade 5 (Linear/Progressiva):")
print(f"V(0.5) = {V_0_5_5:.5f} V")

# --- Atividade 6: I(t) quadrático ---

coef_I6 = regressao(t, I, v_quadratica)
def I_func6(t_val):
    return poly_val(coef_I6, t_val)

def dIdt_func6(t_val):
    return 2 * coef_I6[0] * t_val + coef_I6[1]


V_0_5_6 = L * dIdt_func6(0.5) + R * I_func6(0.5)

print("\nAtividade 6 (Quadrático/Regressiva):")
print(f"V(0.5) = {V_0_5_6:.5f} V")

# --- Atividade 7: I(t) cúbico  ---

coef_I7 = regressao(t, I, v_cubica)
def I_func7(t_val):
    return poly_val(coef_I7, t_val)


def dIdt_func7(t_val):
    return 3 * coef_I7[0] * t_val**2 + 2 * coef_I7[1] * t_val + coef_I7[2]

V_0_5_7 = L * dIdt_func7(0.5) + R * I_func7(0.5)

print("\nAtividade 7 (Cúbico/Central):")
print(f"V(0.5) = {V_0_5_7:.5f} V")

# Atividade 8, 9, 10
def P(r):
    return 3 * (1 - r/4)**(1/7)

def integrand(r):
    return 2 * np.pi * r * P(r)

raios = [1.25, 2.55, 3.15, 3.95]

print("\nAtividade 8 (Ponto Médio):")
for r_val in raios:
    Q = integral(ponto_medio, integrand, 0, r_val, n=1e-4)
    print(f"Q({r_val}) = {Q:.6f}")

print("\nAtividade 9 (Trapézio):")
for r_val in raios:
    Q = integral(trapezio, integrand, 0, r_val, n=1e-4)
    print(f"Q({r_val}) = {Q:.6f}")

print("\nAtividade 10 (Simpson):")
for r_val in raios:
    Q = integral(simpson, integrand, 0, r_val, n=1e-4)
    print(f"Q({r_val}) = {Q:.6f}")