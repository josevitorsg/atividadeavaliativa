# Criando um programa utilizando um vetor de 4 posições 
# onde o usuário irá digitar 4 números.
# o programa irá retornar quantos números negativos foram digitados.

meu_vetor = []

print("NUMEROS NEGATIVOS")
print("Informe 4 números positivos ou negativos ")

# Entrada de dados
for numero in range (4): # ira repetir esse input 4 vezes
    meu_vetor.append(float(input("Digite um número\n")))
# Inicializa o contador de números negativos
quantidade_negativos = 0

# Verifica se cada número é negativo ou positivo
for numero in meu_vetor: #percorre os numeros verificando cada 1
    if numero < 0:
        #Aqui ele soma +1 a variavel quantidade_negativos a cada numero negativo que ele encontrar
        quantidade_negativos += 1

# Exibe a quantidade de números negativos
print(f"\nQuantidade de números negativos digitados: {quantidade_negativos}")