# Criando função para fazer o calculo do valor a pagar
def pagamento (valor_do_cafe, quant): # "pagamento" é o nome da função,  valor_do_cafe e quant é o parâmetro dessa função
  valor_pago = valor_do_cafe * quant # valor_pago é um variavel criada para armazenar o resultado do valor_do_cafe multiplicado pela quantidade.
  return valor_pago # irá retornar o valor que foi armazenado na variavel acima

# Cadastrando o valor 
valor_cafe = float(input("Digite o valor do café: R$:"))

# Quantidade de café desejada
quantidade = int(input("Quantidade de cafés desejada:"))

# Chama a função pagamento com os valores fornecidos e armazena o resultado.
valorapagar = pagamento(valor_cafe, quantidade) #variavel valorapagar irá armazenar o resultado passado pelo função sobre os inputs (passando a função pagamento criada acima, para os inputs valor_cafe e quantidade
print("O Valor a pagar é: ", valorapagar)

