palavra = input("Digite uma frase")
vogais = "aeiouAEIOU"
contador = 0
for letra in palavra:
    if letra in vogais:
     contador += 1
print (f"a frase contém {contador} vogais")