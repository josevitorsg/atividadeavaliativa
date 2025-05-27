
def pagamento (vc, q):
  valor_pago = vc * q
  return valor_pago

# Cadastrando o valor 
valor_cafe = float(input("Digite o valor do café: R$:"))

# Quantidade de café desejada
quantidade = int(input("Quantidade de cafés desejada:"))

# Chama a função pagamento com os valores fornecidos e armazena o resultado.
valorapagar = pagamento(valor_cafe, quantidade)
print("O Valor a pagar é: ", valorapagar)

