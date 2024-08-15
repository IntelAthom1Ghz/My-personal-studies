velocidade = int(input("Digite usa velocidade em km/h:"))
if velocidade > 80:
    multa = (velocidade- 80) * 5
    print(f"Voce excedeu a velocidade permitida, sendo assim você será multado 5 reais por km acima da permitida, logo você pagará um total de {multa} reais de multa")
else:
    print("Sua velocidade está dentro do limite permitido")