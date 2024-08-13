while True:
 try:
     numero = int(input("Digite um número inteiro e positivo"))
     if numero < 0:
      print("Por favor, insira um número válido")
     else:
        break
 except ValueError:
    print("Entrada Inválida!")

#calculo do fatorial

fatorial = 1
for i in range (1, numero + 1):
  fatorial *= i


  print(f"O fatorial de {numero} é {fatorial}")
  