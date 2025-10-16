numero = int(input("Digite um numero inteiro aleatório:"))

resto = numero % 2

print(resto)

if resto == 1:
    print("O valor",numero,"é ímpar")
else:
    print("O valor",numero,"é par")