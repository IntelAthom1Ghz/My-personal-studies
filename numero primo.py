
def eh_primo (num):

    if num <=1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
          return False
    return True


entrada = input( "digite uma lista de números separados por espaço:")

numeros = [int(num) for num in entrada.split()]

if numeros:

    maior = max(numeros)
    menor = min(numeros)

    print (f"O maior número é {maior}.")
    print (f'O menor número é o {menor}.')
else:
    print("Nenhum número foi digitado")



for num in numeros:
    if eh_primo(num):
        print("este número é primo")
    else:
        print("este numero nao é primo")
