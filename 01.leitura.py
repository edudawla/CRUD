
#mostra a lista arquivada
# escritas em um aruivo
arquivo = open('novo.txt', 'r')
lista = (arquivo.readlines())

for i in lista:
    print(i.strip())

print(f'O arquivo tem {len(lista)} cadastros.')

