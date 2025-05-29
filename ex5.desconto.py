# CÁLCULO DE DESCONTO

print("INFORME O VALOR DO PRODUTO:")
v_produto = float(input("R$"))

print("INFORME O PERCENTUAL DE DESCONTO (%)")
p_desconto = float(input())

desconto = v_produto * (p_desconto / 100)
desconto_aplicado = v_produto - desconto

print(f"O PRODUTO SAIRÁ POR R${desconto_aplicado:.2f}")