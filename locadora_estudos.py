kms = int(input("Digite a quantidade de kms rodados:"))
diarias = int(input("Digite a quantidade de dias utilizados:"))
print (f"A quantidade kms rodados de {kms} e a quantidade total de diárias utilizadas é de {diarias}")
     
custo_diaria = diarias * 90
custo_kms = kms * 0.20
custo_total = custo_diaria + custo_kms
print(f" O custo de diárias foi de {custo_diaria} Reais e o de kms rodados foi de {custo_kms} Reais")
print(f"O custo total do aluguel deste carro será de {custo_total} Reais")
