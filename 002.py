
#inserir conteudo ao final
arquivo = open('novo.txt', 'r')

novo = input('Digite a palavra a ser adicionada: ')

arquivo = open('novo.txt', 'a')
arquivo.write(novo)

arquivo.close()
