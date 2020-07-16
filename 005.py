
#apaga palavra
arquivo = open('novo.txt', 'r')
lista = arquivo.readlines()

palavra = input('Digite a palavra a ser buscada: ').upper()

arquivo = open('novo.txt', 'w')
for i in lista:
    if i.strip().upper() != palavra:
        arquivo.write(i)
arquivo.close()

