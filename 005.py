
#apaga palavra
arquivo = open('novo2.txt', 'r')
lista = arquivo.readlines()

palavra = input('Digite a palavra a ser buscada: ').upper()

arquivo = open('novo2.txt', 'w')
for i in lista:
    if i.strip().upper() != palavra:
        arquivo.write(i)
arquivo.close()

