def column_to_dict(data_list, index):
    """Transforma uma coluna da lista de linhas em um dictionary, onde a key é o valor encontrado e o value é o num de ocorrencias.
    INPUT:
    data: list de linhas que serão filtradas pela coluna index,
    ex: { 'foo1', 'bar1', 'foo11' ,'bar11'}
        { 'foo2', 'bar2', 'foo22' ,'bar22'}
        { 'foo3', 'bar3', 'foo22' ,'bar33'}
    index: posiçao da lista que irá ser coletado.
    OUTPUT:
    dicionario: dict dos valores da coluna especificada pelo index.
    ex: column_to_list(data, 2) : {'foo11' : 1, 'foo22' : 2}
    """
    dicionario = {};
    if(type(data_list) is list and type(index) is int):
        for i in range(0, len(data_list)):
            valor = data_list[i][index];
            if(valor in dicionario):
                dicionario[valor] += 1;
            else:
                dicionario[valor] = 1;
        print("[column_to_dict] Dic final  {}.".format(dicionario))
    else:
        print("[column_to_dict] Parametros não atendidos.")
    return dicionario
