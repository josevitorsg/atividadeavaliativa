# CALCULO DE DESCONTO COM CONDIÇÃO:

def desconto(valor):
    if valor > 100:
        valor_do_desconto = valor - (valor * 15) / 100 # Cria uma variavel para armazenar o resultado da conta se o pagamento for mais de 100$
        print("Desconto de 15% ativo.")
        return valor_do_desconto
    else:
        print("Desconto não aplicado, valor minimo de R$100")
        return valor


valor = float(input("\nDIGITE O VALOR DO PRODUTO\n"))

resultado = desconto(valor)

print(f"Você pagará {resultado:.2f} por esta compra!")

