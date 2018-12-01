''' paramter r means readonly '''




''' para fechar automaticamente o arquivo, utilize a funcao with '''
file_data = '';
arquivo="/mnt/crucial/projetos/pessoal/udacity/conceitos-ia/projetos/aula/lendo-escrevendo-arquivos/some_file.txt"
with open(arquivo, 'r') as f:
    file_data = f.read()
    print(file_data)

with open(arquivo, 'w') as f:
    f.write(file_data + " Escrevendo \n Escrevendo")

with open(arquivo, 'r') as f:
    file_data = f.read()
    print(file_data)

with open(arquivo) as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())
