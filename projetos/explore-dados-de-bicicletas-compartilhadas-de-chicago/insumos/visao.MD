# Visão geral

Neste projeto, você utilizará o Python para explorar dados relacionados aos sistemas de compartilhamento de bicicletas nas três maiores cidades dos Estados Unidos: Chicago, Nova Iorque e Washington. Você escreverá um código para importar dados e responder a perguntas interessantes sobre eles, por meio da computação de estatísticas descritivas. Você também vai escrever um script que recebe uma entrada bruta para criar uma experiência interativa no terminal, a fim de apresentar estas estatísticas.

# De que software eu preciso?

Para concluir este projeto, os seguintes requisitos de software são necessários:

Python 3. Os seguintes pacotes da biblioteca padrão do Python provavelmente serão úteis: csv, pprint, datetime e time.
Um editor de texto, como o Sublime ou o Atom.
Um aplicativo terminal (Terminal no Mac e no Linux, ou Cygwin no Windows).


# Detalhes

Na última década, os sistemas de compartilhamento de bicicletas têm crescido em número e popularidade nas cidades de todo o mundo. Sistemas de compartilhamento de bicicletas permitem que os usuários aluguem bicicletas por um período curtíssimo, por um preço específico. Isso permite que pessoas retirem uma bicicleta do ponto A e a devolvam no ponto B, embora também possam devolvê-la no mesmo local, caso queiram apenas sair para um passeio. Independentemente disso, cada bicicleta pode servir vários usuários por dia.

Graças à ascensão das tecnologias de informação, é fácil para um usuário acessar uma estação dentro do sistema para desbloquear ou devolver as bicicletas. Essas tecnologias também fornecem uma riqueza de dados que podem ser utilizados para explorar como esses sistemas de compartilhamento de bicicletas são usados.

Neste projeto, você usará os dados fornecidos pelo Motivate, um provedor de sistema de bicicletas compartilhadas para diversas grandes cidades dos Estados Unidos, para descobrir os padrões de uso do compartilhamento de bicicletas. Você analisará o uso do sistema de uma das maiores cidades dos Estados Unidos: Chicago.

Os conjuntos de dados
Os dados para os primeiros seis meses de 2017 são fornecidos. O arquivo de dados contêm seis (6) colunas principais:

Horário de início (ex., 2017-01-01 00:07:57)
Horário de término (ex., 2017-01-01 00:20:53)
Duração da viagem (em segundos, ex., 776)
Estação inicial (ex., Broadway & Barry Avenue)
Estação final (ex., Sedgwick St & do North Ave)
Tipo de usuário (assinante ou cliente)
Gênero do usuário
Ano de nascimento do usuário
Os arquivos originais - que podem ser acessados aqui: Chicago, Nova Iorque e Washington - tinham mais colunas, e elas diferiam em formato em muitos casos. Alguns processos de data wrangling foram realizados para condensar esses arquivos nas seis colunas principais citadas acima, para simplificar sua análise e a avaliação de suas habilidades de Python. No curso de data wrangling que sucede este curso no programa, os alunos aprendem a manipular os conjuntos de dados mais obscuros e desorganizados, então não se preocupe em perder algo.

As perguntas
Você vai escrever um código para completar as seguintes tarefas sobre os dados de compartilhamento de bicicletas:

Tarefa 1: Mostre as 20 primeiras amostras (linhas) da base de dados
Tarefa 2: Mostre o gênero (coluna) das 20 primeiras amostras
Tarefa 3: Cria uma função para pegar colunas como lista
Tarefa 4: Conte quantas pessoas de cada gênero
Tarefa 5: Crie uma função para contar os gêneros
Tarefa 6: Mostre o gênero mais popular
Tarefa 7: Mostre um gráfico usando os dados anteriores
Tarefa 8: Responda o motivo do número de homens e mulheres não bater com a quantidade de amostras
Tarefa 9: Encontre o valor mínimo, máximo, média e mediana da duração de viagens
Tarefa 10: Mostre todas as estações da base de dados
Tarefa 11: Confira se documentou todas suas funções
Tarefa 12: Crie uma função que conte a ocorrência de qualquer coluna (opcional)
Os arquivos
Para responder a essas perguntas usando o Python, você precisará escrever um script. Para ajudar a orientar seu trabalho neste projeto, fornecemos um modelo com código auxiliar e comentários para download, em formato .py. Você também precisará dos arquivos do conjunto de dados. Todos os arquivos a seguir estão disponíveis para download.

chicago_bikeshare_pt.zip

chicago_bikeshare_pt.py
chicago.csv
Depois de ter baixado este arquivo zip, vá para a próxima página para obter mais detalhes sobre o código que você vai escrever.
