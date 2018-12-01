def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)

    return cast_list

cast_list = create_cast_list('/mnt/crucial/projetos/pessoal/udacity/conceitos-ia/projetos/aula/lendo-escrevendo-arquivos/ex-elenco/lista.txt')
for actor in cast_list:
    print(actor)
