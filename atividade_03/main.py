# Objetivo: Praticar a criação e o uso de módulos e pacotes em Python.
# Módulo: Crie um arquivo chamado matematica.py.
# Neste arquivo, crie as seguintes funções:
    # soma(a, b) que retorna a soma de dois números.
    # subtrai(a, b) que retorna a subtração.
    # modulo(n) que retorna o modulo de um número inteiro positivo.
# Pacote: Crie uma pasta chamada meu_pacote.
# Dentro da pasta, crie:
    # __init__.py (pode estar vazio).
    # mensagens.py com uma função boas_vindas(nome) que retorna a mensagem: "Bem-vindo, [nome]! Vamos aprender Python!"
    # operacoes.py com uma função multiplica(a, b) que retorna a multiplicação.
# Usando Módulos e Pacotes: Crie um arquivo principal chamado main.py.
    # Importe o módulo matematica.
    # Importe os módulos do pacote meu_pacote.
    # Mostre a mensagem de boas-vindas usando boas_vindas("SeuNome").
    # Realize e imprima os resultados de:
    # soma(5, 2)
    # subtrai(10, 4)
    # modulo(5)
    # multiplica(3, 7)

import matematica
from meu_pacote import mensagem
from meu_pacote import operacoes

mensagem.boas_vindas("Olga")

print("Soma:", matematica.soma(5, 2))
print("Subtração:", matematica.subtrai(10, 4))
print("Módulo:", matematica.modulo(5))
print("Multiplicação:", operacoes.multiplica(3, 7))