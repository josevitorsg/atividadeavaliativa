# SOLICITAR AO USUARIO DOIS VALORES EM VARIAVEIS DIFERENTES E MUDAR O VALOR DE UMA VARIAVEL POR OUTRA.

print("DIGITE UM NÚMERO PARA A VARIAVEL A:")
a = int(input())

print("DIGITE UM NÚMERO PARA VA VARIAVEL B: ")

b = int(input())

print(f"Antes da troca: A={a}, B={b}")

a, b = b, a # Aqui acontece a troca. 

print (f"Depois da troca: A={a}, B={b} ")

# Atribuição multipla (a, b = b, a )é a forma altamente recomendada
# e mais "pythonica" de trocar valores de variáveis em python, ela é concisa,
# legível e eficiente.
