import random
numero_secreto = random.randint (1,100)
tentativas = 0

print("Eu estou pensando em um número entre 1 e 100")
while True:
 try:
     palpite = int(input("Tente adivinhar"))
     tentativas += 1
     if palpite < numero_secreto:
         print("Muito baixo!, tente novamente")
     elif palpite > numero_secreto:
         print ("Muito alto, tente novamente")
     else:
         print (f"Correto! Você adivinhou em {tentativas} tentativas")
         break
 except ValueError:
    
    print ("Entrada inválida")