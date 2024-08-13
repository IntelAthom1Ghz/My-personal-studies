def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "ERRO: Divisão por zero!"

def calculadora():
    print("Escolha uma opção:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação (1/2/3/4): ")

    if escolha in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"O resultado da adição é: {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"O resultado da subtração é: {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"O resultado da multiplicação é: {multiplicar(num1, num2)}")
            elif escolha == '4':
                print(f"O resultado da divisão é: {divisao(num1, num2)}")

        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite números válidos.")
    else:
        print("Erro: Escolha inválida. Por favor, selecione uma opção válida.")

# Chama a função da calculadora
calculadora()