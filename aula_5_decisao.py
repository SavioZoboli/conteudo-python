media = float(input("Digite o valor da média: "))

if media < 0 or media > 10:
    print("média inválida")
    exit(1)

if media >= 7:
    print("Parabéns, você está aprovado! 😊")
elif media >= 3:
    print("Atenção, você está de exame! 🤣")
else:
    print("Que pena, você está reprovado! 😒")






