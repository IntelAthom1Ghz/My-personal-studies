import datetime
agora = datetime.datetime.now()
data_nascimento = int(input("Digite o ano em que você nasceu:"))
idade = agora.year - data_nascimento
if idade > 15:
    print("Você possui idade suficiente e dentro da lei para exercer seu direito de voto!")
else:
    print("Você não possui idade suficiente segundo a lei para exerceu o seu direito de voto!")