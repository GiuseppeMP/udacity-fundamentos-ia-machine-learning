''' paramter r means readonly '''

arquivo="/mnt/crucial/projetos/pessoal/udacity/conceitos-ia/projetos/aula/lendo-escrevendo-arquivos/some_file.txt"

f = open(arquivo, 'r')
file_data = f.read()
print(file_data)
f.close()


f = open(arquivo, 'w')
f.write(file_data + " Escrevendo \n Escrevendo")
f.close()


f = open(arquivo, 'r')
file_data = f.read()
print(file_data)
f.close()
