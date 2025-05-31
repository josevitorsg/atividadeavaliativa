# CLASSIFICAÇÃO DE TRIÂNGULOS

def verificar_area(a, b, c):
    """Classificando um triangulo com base no comprimento
    dos seus lados"""
    if a + b <= c or a + c <= b or b + c <= a:
        # Se a + b é menor ou igual a c, irá retornar que nao é um triangulo. (assim por diante)
        return "Não é um triangulo"
    if a == b == c:
        return "Equilatero"
    # Se um dos lados tiver a medida igual a apenas 1 outro lado, ele retorna isosceles 
    elif a == b or a == c or b == c: 
        return "Isósceles"
    # Se todos lados forem diferentes, ele retorna Escaleno.
    else:
        return "Escaleno"

print("\nCLASSIFICANDO TRIANGULOS")

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Digite um número valido.")
else:
    area_triangulo = verificar_area(lado1, lado2, lado3)
    print(f"O Triângulo é: {area_triangulo}")

