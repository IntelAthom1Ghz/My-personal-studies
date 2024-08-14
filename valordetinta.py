largura = float(input("Digite a largura da parede em metros quadrados:"))
altura = float(input("Dgigite a altura da parede em metros quadrados:"))

area_parede = largura * altura
tinta_necessaria = area_parede /2
valor = tinta_necessaria * 2.45
print(f"Sua parede possui um total de {area_parede:.2f} metros quadrados de área, sendo assim será necessário {tinta_necessaria:.2f} Litros de tinta para pintar, resultando em um valor de {valor:.2f} Reais")

