
#verificar quantidade de linhas
# escritas em um aruivo
arquivo = open('novo.txt', 'r')

conteudo = []
for linha in arquivo:
    linha = linha.strip()
    conteudo.append(linha)
print(f'O arquivo selecionado tem {len(conteudo)} linhas')
arquivo.close()
