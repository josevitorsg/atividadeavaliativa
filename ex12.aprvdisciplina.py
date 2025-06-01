# Aprovando em disciplina

def aprovacao (nota):
    if nota >= 7:
        return "APROVADO!"
    else:
        return "REPROVADO!"


nota_aluno = float(input(f"\nDigite sua nota: "))

resultado = aprovacao(nota_aluno) # definindo uma variavel e chamando a função definida acima para verificar a nota do aluno.

print(f"Sua nota foi {nota_aluno:.2f}, e você está {resultado}")


