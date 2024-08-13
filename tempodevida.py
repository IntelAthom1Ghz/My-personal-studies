data = input("Digite sua data de nascimento:")
ultimos_4_digitos = int(data[-4:])
anos = 2024 - ultimos_4_digitos

print (f"você nasceu em {data} e hoje você  tem {anos}" )
