
#inserir conteudo ao final
arquivo = open('novo.txt', 'r')
lista = arquivo.readlines()

novo = input('Digite a palavra a ser adicionada: ')
lista.append(f'{novo}\n')

arquivo = open('novo.txt', 'w')
for i in lista:
    arquivo.writelines(i)

arquivo.close()
