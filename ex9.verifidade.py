# Verificação de idade para dirigir.

def  maior_de_idade(idade): # Cria uma função chamada maior_de_idade que recebe o parâmetro idade
    if idade >= 18:
        return True # A funçao ira retornar TRUE se a idade do usuario for maior ou igual a 18
    else:
        return False # Se a idade for menos que 18 ela ira retornar false


print("\nVERIFICAÇÃO DE IDADE PARA DIRIGIR")

idade_usuario = float(int(input("\nQual sua idade? ")))
 

if maior_de_idade(idade_usuario):
    print("PERMITIDO!")
else:

    print("Ainda não possui idade suficiente!")
