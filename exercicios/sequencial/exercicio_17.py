area = float(input("Insira a quantidades em m² a ser pintada: "))

cob_tinta = 6
val_tinta_g = 80
val_tinta_p = 25

nec_tinta = area/6
nec_tinta = nec_tinta * 1.1

print("Necessário: ",nec_tinta,"l de tinta (com 10% de margem) \n")

print("### 1ª situação ###")

qtd_tinta_g = nec_tinta/18

sobra_tinta = 0

if qtd_tinta_g//1 != qtd_tinta_g:
    qtd_tinta_g = qtd_tinta_g//1 + 1
    sobra_tinta = qtd_tinta_g * 18 - nec_tinta

valor_total = qtd_tinta_g * val_tinta_g

print("Utilizando apenas latas de 18 litros você tem:")
print("Quantidade de latas: ",qtd_tinta_g)
print("Valor total: R$",valor_total)
print("Desperdício: ",sobra_tinta,"l")

print("\n")

print("### 2ª Situação")

qtd_tinta_p = nec_tinta/3.6

sobra_tinta = 0

if qtd_tinta_p//1 != qtd_tinta_p:
    qtd_tinta_p = qtd_tinta_p//1 + 1
    sobra_tinta = qtd_tinta_p * 3.6 - nec_tinta

valor_total = qtd_tinta_p * val_tinta_p

print("Utilizando apenas latas de 3.6 litros você tem:")
print("Quantidade de latas: ",qtd_tinta_p)
print("Valor total: R$",valor_total)
print("Desperdício: ",sobra_tinta,"l")

print("\n")

print("### 3ª situação ###")

qtd_tinta_g = nec_tinta/18
qtd_tinta_p = 0
sobra_tinta = 0

if qtd_tinta_g//1 != qtd_tinta_g:
    qtd_tinta_g = qtd_tinta_g//1
    qtd_tinta_p = (nec_tinta - (qtd_tinta_g * 18) )/ 3.6
    if qtd_tinta_p // 1 != qtd_tinta_p:
        qtd_tinta_p = qtd_tinta_p//1 + 1
        sobra_tinta = (qtd_tinta_p * 3.6 + qtd_tinta_g * 18) - nec_tinta

valor_total = qtd_tinta_g * val_tinta_g + qtd_tinta_p * val_tinta_p

print("Utilizando latas de 18l e 3.6l você tem:")
print("Quantidade de latas: G:",qtd_tinta_g," P:",qtd_tinta_p)
print("Valor total: R$",valor_total)
print("Desperdício: ",sobra_tinta,"l")