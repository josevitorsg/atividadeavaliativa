# CLASSIFICAÇÃO DE IDADE


def classificar (idade):
    if idade <= 14:
        return "uma Criança"
    elif 14 <= idade <= 18: # se idade é maior q 14 e menor q 18
        return "um Adolescente"
    elif 18 <= idade <= 30:
        return "um Adulto Jovem"
    else:
        return "um Adulto"
    

print("Digite sua idade:")

idade = int(input())

classificando = classificar(idade)

print(f"Esta pessoa é {classificando}!")


