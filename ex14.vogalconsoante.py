# VERIFICAÇÃO DE VOGAL OU CONSOANTE

def vogais(letras):
    letras = letras.lower() # CONVERTE PARA MINUSCULA PARA FICAR FACIL A COMPARAÇÃO
    if letras in 'aeiou': # verifica se a letra é uma vogal
        return "VOGAL"
    else: # se nao estiver dentro do 'aeiou' é uma consoante.
        return "CONSOANTE"
    

print("\nVERIFICAÇÃO DE VOGAL OU CONSOANTE")

letra = str(input("Digite uma letra ara verificar: "))

vogal_ou_consoante = vogais(letra) # passa a letra digitada do usuario dentro da função para verificar


print(vogal_ou_consoante)

