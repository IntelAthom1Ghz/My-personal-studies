def obter_numero_valido(prompt):
    while True:
        entrada = input(prompt)
        if entrada.lower() == 'sair':
            return entrada       
        if entrada.replace('.', '', 1).isdigit() or entrada.replace('-', '', 1).replace('.', '', 1).isdigit():
            return float(entrada)
        else:
            print("Entrada inválida. Por favor, insira um número.")

total_renda = 0

while True:
    renda = obter_numero_valido("Digite o valor de sua renda durante os últimos 12 meses (digite 'sair' para encerrar): ")
    #condição para sair do loop
    if renda == 'sair':
        break
    #####################
    #total da renda
    total_renda += renda

print(f"A sua renda anual é: {total_renda:.2f}")

#calcular o imposto do caba de acordo com a renda
if total_renda <= 24511.92:
    print("Sua alíquota de imposto a ser paga é zero, sua renda anual não se enquadra como pagante de imposto de renda!")
elif total_renda >= 24511.93 and  total_renda <= 33919.80:
    calculo_caso1 = total_renda * 7.5/100
    print(f"Sua renda anual se enquadra na alíquota de 7,5%, sendo assim você deverá pagar {calculo_caso1} de imposto")
elif total_renda >= 33919.81 and total_renda <= 45012.60:
    calculo_caso2 = total_renda * 15/100
    print(f"Sua renda anual se enquadra na alíquota de 15%, sendo assim você deverá pagar {calculo_caso2} de imposto")
elif total_renda >= 45012.61 and total_renda <= 55976.91:
    calculo_caso3 = total_renda * 22.5/100 
    print(f"Sua renda anual se enquadra na alíquota de 22,5%, sendo assim você deverá pagar {calculo_caso3} de imposto")   
else:
    calculo_caso4 = total_renda * 27.5/100
    print(f"Sua renda anual se enquadra no último caso tabelado, sendo este com uma alíquota de 27,5%, sendo assim você deverá pagar {calculo_caso4} de imposto")