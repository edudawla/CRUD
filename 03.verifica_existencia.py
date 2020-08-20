
#verifica existencia de palavra na lista
palavra = input('Digite a palavra a ser buscada: ').upper()
arquivo = open('novo.txt', 'r')

cont = 0
for i in arquivo:
    if i.strip().upper() == palavra:
        cont+=1;
if cont > 0:
    print(f'a palavra {palavra} existe {cont} na lista')
else:
    print(f'a palavra escolhida {palavra } ainda NAO foi cadastrada')

