"""
Calculadora de IMC
"""

print("Vamos calcular seu imc!")
alt = float(input("Digite sua altura: "))
peso= float(input("Favor digitar seu peso: "))

calc_imc = peso / (alt * alt)

print(f"Seu imc é {calc_imc:.2f}")