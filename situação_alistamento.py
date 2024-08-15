import datetime
agora = datetime.datetime.now()

ano = int(input("Digite seu ano de nascimento:"))
idade_atual = agora.year - ano
print(f"Sua idade atual é de {idade_atual} anos")
qualto_falta = 18 - idade_atual
quanto_passou = idade_atual - 18

if idade_atual < 18:
    print(f"Calma la rapaz, sua hora vai chegar, ainda falta {qualto_falta} ano(s) para você se alistar")
elif idade_atual == 18:
 print(f"Meus parabéns (ou não), você está na idade para se alistar ao exército brasileiro!")
else:
   print(f"Você já está velho, ja se passaram {quanto_passou} anos desde seu alistamento!")    