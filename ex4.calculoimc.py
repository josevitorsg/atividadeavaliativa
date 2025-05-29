
while True:
    print("\n1 - CALCULAR IMC\n2 - Sair")
    opcao = int(input("Selecione uma opção:"))

    if opcao == 1:
        print("CALCULADORA DE IMC")
        print()

        print("INFORME SEU PESO(kg)")
        peso = float(input())
        print("INFORME SUA ALTURA(metros)")
        altura = float(input())
        imc = peso / (altura * altura)
        print("SEU IMC É DE ", imc)

    
    else:
        print("Saindo do programa...")
        break



