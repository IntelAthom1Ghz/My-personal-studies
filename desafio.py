começou_fumar = int(input("Insira aproximadamente a idade com qual você começou a fumar:"))
idade_atual = int(input("Insira sua idade atual:"))
cigarros_diarios = int(input("Insira quantos cigarros em media você fuma por dia:"))

total_ja_fumado_idade = idade_atual - começou_fumar 
total_cigarro_fumado = total_ja_fumado_idade * 365 * cigarros_diarios
tempo_de_redução_diário = cigarros_diarios * 1/6 #em horas
tempo_diario_em_dias = tempo_de_redução_diário / 24
tempo_total_desde_o_começo = total_cigarro_fumado *1/6 /24

print(f" você ao todo ja fumou {total_cigarro_fumado} de cigarros em sua vida")
print(f" O tempo de redução de vida diário seguindo sua media de uso, é de {tempo_diario_em_dias:.2f} dias")
print(f"Seu tempo total de redução de vida desde o começo de seu uso de cigarro até os dias atuais, considerando que cada cigarro fumado reduz em média 10 minutos de vida (ou 1/6 de hora) é de {tempo_total_desde_o_começo:.2f} dias de vida")


