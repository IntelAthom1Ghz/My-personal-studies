from collections import Counter
import re 

frase = input("Digite uma frase")
frase_limpa = re.sub(r'[^\w\s]', '', frase).lower()

palavras = frase_limpa.split()

contagem = Counter(palavras)
print ("palavras que aparecem mais de uma vez")
for palavra, frequencia in contagem.items():
   if frequencia >1:
      print (f"A palavra {palavra} aparece {frequencia} vezes")
