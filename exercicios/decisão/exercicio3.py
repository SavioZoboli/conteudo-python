print("M - Masculino | F - Feminino | O - Outros")
sexo = input("Qual é o seu sexo? ")

if sexo == "F":
    print("Você escolheu a opção Feminino")
elif sexo == "M":
    print("Você escolheu a opção Masculino")
else:
    print("Você escolheu a opção Outros")

match sexo:
    case "F":
        print("Você escolheu a opção Feminino")
    case "M":
        print("Você escolheu a opção Masculino")
    case _:
        print("Você escolheu a opção Outros")