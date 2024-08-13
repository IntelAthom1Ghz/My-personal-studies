# Solicitar entrada do usuário como string para poder verificar se é um número válido
numero_str = input("Digite um número inteiro positivo: ")

# Verificar se a entrada é válida (apenas dígitos e positivo)
while not numero_str.isdigit():
    numero_str = input("Entrada inválida. Por favor, insira um número inteiro positivo: ")

# Converter a string para inteiro após validação
numero = int(numero_str)

# Calcular a soma dos dígitos
soma_digitos = sum(int(digito) for digito in numero_str)

# Exibir o resultado
print(f"A soma dos dígitos de {numero} é {soma_digitos}.")