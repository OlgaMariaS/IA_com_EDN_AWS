# EXERCÍCIO PRÁTICO 1​
# Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. 
# A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:​
#     - A calculadora deve solicitar ao usuário que insira dois números e uma operação.​
#     - As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).​
#     - O programa deve continuar solicitando entradas até que uma operação válida seja concluída.​

# Trate os seguintes erros:​
#     - Entrada inválida (não numérica) para os números​
#         - Divisão por zero​
#         - Operação inválida​
#     - Use try/except para capturar e tratar os erros apropriadamente.​
#     - Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.​

# Quando uma operação é concluída com sucesso, exiba o result e encerre o programa.​

while True:
    # Solicitar o primeiro número
    while True:
        try:
            number1 = float(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número válido.")
    
    # Solicitar o segundo número
    while True:
        try:
            number2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número válido.")
    
    # Solicitar a operação
    while True:
        operation = input("Digite a operação (+, -, *, /): ").strip()
        if operation in {'+', '-', '*', '/'}:
            break
        else:
            print("Erro: Operação inválida. Por favor, escolha entre +, -, *, /.")
    
    # Realizar cálculo e tratar divisão por zero
    try:
        if operation == '+':
            result = number1 + number2
        elif operation == '-':
            result = number1 - number2
        elif operation == '*':
            result = number1 * number2
        elif operation == '/':
            result = number1 / number2
        
        print(f"Resultado de {number1} {operation} {number2} = {result}")
        break  # Encerrar o programa 
    
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida. Tente novamente.")