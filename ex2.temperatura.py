
#Define a função para conversão;
def conversor(celsius):
  return (celsius * 9/5) + 32



# Solicita a temperatura em Celsius ao usuário:
celsius = float(input("Celsius: "))

# chama a funçãop e armazena o resultado
fahrenheit = conversor(celsius)

# Exibe o resultado
# o f antes da string ativa a f-string (mais legivel, mais conciso
# permite expressoes dentro das chaves {}, permite formatação (como arredondamento de números))

print(f"Fahrenheit: {fahrenheit} °F")
