# CALCULADORA DE JUROS SIMPLES

print ("CALCULADORA DE JUROS SIMPLES")

print ("Digite o valor:")
valor = float(input())

print("Taxa de juros:")
juros = float(input())

print("Número de Anos: ")
anos = float(input())

montante = valor + (valor * juros * anos / 100)

print(f"Você pagará um total de R${montante:.2f}")


