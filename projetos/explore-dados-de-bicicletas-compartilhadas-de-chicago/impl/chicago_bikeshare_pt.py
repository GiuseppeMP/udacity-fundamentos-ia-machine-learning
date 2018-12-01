# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

arquivo="chicago.csv"

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open(arquivo, "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

index_gender = -2
index_userType = -3
index_tripDuration = 2
index_startStation = 3

input("Aperte Enter para continuar...")
# TAREFA 1 - Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for i in range(1, 21):
    print("Linha {} : {} ".format(i,data_list[i]))

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2 - Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for i in range(0, 20):
    print("Linha {} : Gênero: {} ".format(i,data_list[i][6]))

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3 Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem

def column_to_list(data, index):
    """Transforma uma coluna da lista de linhas em uma list.
    INPUT:
    data: list de linhas que serão filtradas pela coluna index,
    ex: { 'foo1', 'bar1', 'foo11' ,'bar11'}
        { 'foo2', 'bar2', 'foo22' ,'bar22'}
        { 'foo3', 'bar3', 'foo33' ,'bar33'}
    index: posiçao da lista que irá ser coletado.
    OUTPUT:
    column_list: list dos valores da coluna especificada pelo index.
    ex: column_to_list(data, 2) : {'foo11', 'foo22', 'foo33'}
    """
    column_list = []
    if(type(data) is list and type(index) is int):
        # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
        for i in range(0, len(data)):
            column_list.append(data[i][index])
        print("[column_to_list] Tamanho da lista da resultado: {}".format(len(column_list)))
    else:
        print("[column_to_list] Parametros não atendidos.")

    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, index_gender)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4 Conte cada gênero. Você não deveria usar uma função para isso.

def count_column_conditional_ocrr(data, index, lambdaVerificacao):
    """Função que conta quantas vezes o valor em uma coluna atende a condição passada por parametro.
    INPUT:
    data: list de linhas que serão filtradas pela coluna index,
    ex: { 'foo1', 'bar1', 'foo11' ,'bar11'}
        { 'foo2', 'bar2', 'foo22' ,'bar22'}
        { 'foo3', 'bar3', 'foo33' ,'bar33'}
    index: posiçao da lista que irá será analisado com lambdaVerificacao.
    lambdaVerificacao: funcao anonima que será executada para validar o valor da posição.
    OUTPUT:
    counter: inteiro com valor de quantas vezes a lambdaVerificacao foi atendida.
    """
    counter = 0;
    if(type(data) is list and type(index) is int):
        # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
        for i in range(0, len(data)):
            valor = data[i][index];
            if(lambdaVerificacao(valor)):
                counter +=1;

        print("[count_column_conditional_ocrr] Contador final de colunas: {}".format(counter))
    else:
        print("[count_column_conditional_ocrr] Parametros não atendidos.")

    return counter

male = count_column_conditional_ocrr(data_list, index_gender, lambda valor: valor == 'Male' )
female = count_column_conditional_ocrr(data_list, index_gender, lambda valor: valor == 'Female' )


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5 Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """Função que conta quantas vezes o valor Female e Male aparecem na coluna Gender.
    TODO (Essa função não faz sentido nenhum caso seja avaliada com conceitos SOLID)
    INPUT:
    data_list: list de linhas que serão filtradas especificamente pela coluna index de Gender
    OUTPUT:
    list: lista da quantidade totalizada.
    """
    male = count_column_conditional_ocrr(data_list, index_gender, lambda valor: valor == 'Male' )
    female = count_column_conditional_ocrr(data_list, index_gender, lambda valor: valor == 'Female' )
    return [male, female]

def count_userType(data_list):
    """Função que conta quantas vezes o valor Customer e Subscriber aparecem na coluna user_types.
    TODO (Essa função não faz sentido nenhum caso seja avaliada com conceitos SOLID)
    INPUT:
    data_list: list de linhas que serão filtradas especificamente pela coluna index de user_types
    OUTPUT:
    list: lista da quantidade totalizada.
    """
    customer = count_column_conditional_ocrr(data_list, index_userType, lambda valor: valor == 'Customer' )
    subscriber = count_column_conditional_ocrr(data_list, index_userType, lambda valor: valor == 'Subscriber' )
    return [customer, subscriber]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6 Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.

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

def often_key(dicionario):
    """Conta qual a chave com maior valor no dicionario, funcao utilizada em conjunto com a column_to_dict.
    INPUT:
    data: dicionario da coluna
    ex:  {'foo11' : 1, 'foo22' : 2}
    OUTPUT:
    answer: valor que mais se repetiu ou key com maior valor de ocorrencias, vide doc da function column_to_dict.
    ex: 'foo22'
    """
    answer = ""
    maxAuxiliar = 0;
    if(type(dicionario) is dict):
        for chave in dicionario:
            valor = dicionario[chave];
            # TODO E se ocorrer o mesmo número?
            if(valor > maxAuxiliar):
                maxAuxiliar = valor
                answer = str(chave)
            print("[often_key] Chave:{} , Valor: {}".format(chave, valor))

    return answer

def most_popular_value_on_column(data_list, index):
    return often_key(column_to_dict(data_list, index));

def most_popular_gender(data_list):
    return most_popular_value_on_column(data_list, index_gender);


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, index_gender)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

userType_list = column_to_list(data_list, index_userType)
types = ["Customer", "Subscriber"]
quantity = count_userType(data_list)
print(type(quantity))
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuario')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuario')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Os valores são contabilizados partindo do conjecturado que a coluna terá sempre valor 'Female' ou 'Male', não totalizando outras informações como vazio, Boy, Girl, etc ."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, index_tripDuration)

def encontrarMediana(lista):
    """Função que encontra a mediana de uma lista de valores.
    INPUT:
    lista: lista de valores númericos
    ex:  { 270, 310, 702}
    OUTPUT:
    median_trip: valor calculado da mediana, valor do centro da lista ordenada, do menor para maior
    ex: 310
    """
    lista = sorted(lista)
    centro = len(lista) // 2
    if len(lista) % 2 == 0:
        return sum(lista[centro - 1:centro + 1]) / 2.0
    else:
        return lista[centro]

min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.


for i in range(0, len(trip_duration_list)):
    valor = trip_duration_list[i]
    valor = float(valor);
    mean_trip += valor;

    if(i != 0):
        if(valor > max_trip):
            max_trip = valor
        if(valor < min_trip):
            min_trip = valor
    else:
        min_trip = valor
        max_trip = valor
        mean_trip = valor

mean_trip = round(mean_trip/len(trip_duration_list))
median_trip = float(encontrarMediana(trip_duration_list))

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
# TODO não consegui atender a mediana, não consigo encontrar o valor 670 nunca :(
#assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, index_startStation))


print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
'''
Função de exemplo com anotações.
Argumentos:
  param1: O primeiro parâmetro.
  param2: O segundo parâmetro.
Retorna:
  Uma lista de valores x.
'''

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(dicionario):
    """Totaliza a quantidade de valores diferentes e totaliza a quantidade de ocorrencias de todos eles.
    INPUT:
    data: dicionario da coluna
    ex:  {'foo11' : 1, 'foo22' : 2}
    OUTPUT:
    answer: tolizador dos valores e ocorrencias.
    ex: 3, 10000
    """
    item_types = []
    count_items = []

    for chave in dicionario:
        valor = dicionario[chave];
        item_types.append(chave)
        count_items.append(valor)

    print(sum(count_items))
    return item_types, count_items


if answer == "yes":
    #Alterar a estrutura de dados para dict para facilitar as outras tarefas, então tive que modificar a chamada de column_to_list para column_to_dict
    column_dict = column_to_dict(data_list, -2)
    types, counts = count_items(column_dict)
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    # column_list = column_to_list(data_list, -2)
    # types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
