"""
Divisor, fazer um algoritmo faz que a divisão e caso o divisor for 0 mostrar na tela uma mensagem.
"""

print("Vamos fazer uma divisão!")
num1 = int(input("Digite seu dividendo: "))
num2 = int(input("Digite seu divisor: "))
resultado = ""


if num2 == 0:
    print("Favor digitar um número maior que 0")
    
else:
    resultado = int(num1 / num2)

print(f"O resultado da divisão de {num1} com {num2} é {resultado}")

