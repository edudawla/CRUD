from pathlib import Path

arquivo = input('digite o nome do arquivo: ') #'novo.txt'
nome = Path(arquivo+'.txt')

if nome.is_file(): #nome é arquivo?
    file = open(nome, 'r')
    lista = file.readlines()
    print('o arquivo existe e tem:')
    for i in lista:
        print(i.strip)
    print(f'{len(lista)} cadastros.')

else:
    print('arquivo inexistente')
