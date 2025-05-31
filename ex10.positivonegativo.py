# VERIFICAÇÃO DE NUMERO POSITIVO OU NEGATIVO.

def verifica (numero):
    if numero > 0:
        print (f"O número {numero:.0f}, é positivo!")
    elif numero < 0:
        print (f"O número {numero:.0f}, é negativo!")
    elif numero == 0:
        print (f"O número {numero:.0f}, é zero!")
    


print ("\nVERIFICAR SE UM NÚMERO É POSITIVO OU NEGATIVO")

numero_digitado = float(input("\nDigite um número para verificar: "))

verifica(numero_digitado) # Chama a função "verifica" para verificar o número digitado pelo usuario.


