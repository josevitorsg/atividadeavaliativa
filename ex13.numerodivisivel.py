# Verificando se um número é divisivel por 3 e 5

def divisivel(algaritmo):
    if algaritmo % 15 == 0: # % retorna o resto da divisão de ambos operandos
        return True # Se o número for divisivel por 3 e 5 entao o numero sera divisivel or 15
    #por que 3x5 = 15, ai é so verificar se um número é divisivel por 15 usando numero % 15 == 0
    else:
        return False
    




print ("\nDIGITE UM NÚMERO PARA VERIFICAR: ")

numero = int(input())

if divisivel(numero):
    print(f"O número {numero} é divisivel por 3 e 5!")
else:
    print(f"O número {numero} não é divisivel por 3 e 5.")




