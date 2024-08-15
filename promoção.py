nome = input("Digite seu nome completo:")
sexo = input("Digite seu sexo (masculino ou feminino):").strip().lower()
valor_compra = float(input("Digite o valor da compra:"))
print(f" Seu nome é {nome} e seu sexo é {sexo}") 
try:
    if sexo == 'masculino':
       calcular_desconto_homem = valor_compra * 5/100
       valor_compra_com_desconto_homem = valor_compra - calcular_desconto_homem
       print(f"Seu desconto será de {calcular_desconto_homem:.2f} reais")
       print(f"O total da sua conta com o desconto será de {valor_compra_com_desconto_homem:.2f}")
    elif sexo == 'feminino':
       calculo_desconto_mulher = valor_compra * 13/100
       valor_compra_com_desconto_mulher = valor_compra - calculo_desconto_mulher
       print(f"Seu desconto será de {calculo_desconto_mulher:.2f} reais")
       print(f"O total da sua conta com o desconto será de {valor_compra_com_desconto_mulher:.2f}reais")
    else:
       print("Sexo invalido. Digite 'masculino' ou 'feminino'.")

except ValueError:
   print("Ocorreu um erro ao processar a compra, verifique os valores que foram digitados")

#########
