# Criar e escrever 3 frases com 'w'
arquivo = open('minhas_notas.txt', 'w')
arquivo.write("Estou estudando python\n")
arquivo.write("Aprendendio a manipular arquivos\n")
arquivo.write("Este é o conteúdo inicial do arquivo\n")
arquivo.close()

# Acrescentar 2 frases com 'a'
arquivo = open('minhas_notas.txt', 'a')
arquivo.write("Agora estamos adicionando mais conteúdo\n")
arquivo.write("Fim!\n")
arquivo.close()

# Ler e imprimir com with
with open('minhas_notas.txt', 'r') as arquivo:
    conteudo = arquivo.read()
print(conteudo)