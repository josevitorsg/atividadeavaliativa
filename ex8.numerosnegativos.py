# Criando um programa utilizando um vetor de 4 posições 
# onde o usuário irá digitar 4 números.
# o programa irá retornar quantos números negativos foram digitados.

meu_vetor = []

print("NUMEROS NEGATIVOS")
print("Informe 4 números positivos ou negativos ")
meu_vetor.append(float(input("Digite o primeiro número: ")))
meu_vetor.append(float(input("Digite o segundo número: ")))
meu_vetor.append(float(input("Digite o terceiro número: ")))
meu_vetor.append(float(input("Digite o quarto número: ")))

for numero in meu_vetor:
    if numero < 0:
        print(f"O número {numero}, é negativo")
    
    elif numero == 0:
        print("O número é zero")

    else:
        print(f"O número {numero}, é positivo.")