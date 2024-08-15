nome = input("Digite seu nome completo:")
nota_1 = float(input("Digite sua primeira nota:"))
nota_2 = float(input("Digite sua segunda nota:"))
print(f" Bem vindo {nome}, sua primeira nota é {nota_1} e a segunda é {nota_2}")

media = (nota_1 + nota_2) / 2

if media > 7 :
    print(f"Parabéns, você conseguiu uma média de {media}, você teve um ótimo aproveitamento, continue assim!")

else:
    print(f"Se esforce mais, você ficou com uma média de {media}, ficando abaixo da linha de corte para bom aproveitamento")