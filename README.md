# How to create enviroment with conda

To create an environment:

>`conda create --name myenv`

Create the environment from the environment.yml file:

>`conda env create -f environment.yml`

To create an enviroment for the udacity class room:
>`conda create -n udacity-fundamentos-ia numpy jupyter notebook  pandas matplotlib seaborn python=3`

Activate & Deactivate enviroment

>`source activate udacity-fundamentos-ia`

>`source deactivate`

To list enviroments

>`conda env list`


# to run a jupyter notebook just run the code below on terminal or console:
>$`jupyter notebook`






# 01/DEC/18 Repository Init


## Organização README.md


### fix CVE-2018-18074.
>More information
>moderate severity
>Vulnerable versions: <= 2.19.1
>Patched version: 2.20.0
>The Requests package through 2.19.1 before 2018-09-14 for Python sends an HTTP Authorization header to an http URI upon receiving a same-hostname https-to-http redirect, which makes it easier for remote attackers to >discover credentials by sniffing the network.


# 01/DEC/2018 Entrega 2° Projeto - "Prevendo o preço dos imóveis residenciais em Boston - Udacity" 


## Briefing do Projeto

O mercado imobiliário de Boston é altamente competitivo, e você quer ser o melhor corretor de imóveis da região. Para competir com seus colegas, você decidiu elencar alguns conceitos básicos de Machine Learning para ajudar você e seu cliente a acharem o melhor preço de venda para a casa dele. Com sorte, você se deparou com o conjunto de dados de habitação de Boston, que contém dados agregados de várias características para casas das comunidades da Grande Boston, incluindo o valor médio das casas para cada uma das regiões. Sua tarefa é construir um modelo ótimo, baseado na análise das estatísticas com as ferramentas disponíveis. Esse modelo será, então, usado para estimar o melhor preço de venda para a casa de seus clientes.

> folder -> projetos/prevendo-preco-imoveis-residencias-boston

# 01/DEC/18 Aula 2 - Estatística Descritiva - Parte II

## Aula 2: Lecture 01. O que são medidas de dispersão?


Medidas de dispersão (spread) são usadas para nos dar uma ideia do quão dispersos nossos dados são um do outro. Medidas comuns de dispersão incluem:


1. Amplitude
2. Amplitude interquartil (IQR)
3. Desvio-padrão
4. Variância


## Aula 2: Lecture 02. Histogramas

Histogramas são super úteis para compreender os diferentes aspectos de dados quantitativos. Nos tópicos a seguir você verá histogramas sendo usados o tempo todo para ajudar você a compreender os quatro aspectos que destacamos anteriormente sobre uma variável quantitativa:

1. Centro
2. Dispersão
3. Forma
4. Outliers

## Aula 2: Lecture 03. Dias úteis x fins de semana - qual a diferença?

É  possível observar que o número de cães é igual durante a semana e no fins de semana mas a propagação varia.


## Aula 2: Lecture 04. Introdução ao resumo de cinco números.


Calculando o five number summary (resumo em cinco números)

O five number summary consiste em 5 valores:

    > **Mínimo**: O menor número no conjunto de dados.
    > **Q1**​: O valor de tal forma que 25% dos dados sejam menores que ele.
    > **Q2**​: O valor tal que 50% dos dados sejam menores que ele.
    > **Q3**​: O valor de tal forma que 75% dos dados sejam menores que ele.
    > **Máximo**: O maior valor no conjunto de dados.

No vídeo acima nós vimos que calcular cada um desses valores era essencialmente encontrar a mediana de vários conjuntos de dados diferentes. Porque nós estamos, essencialmente, calculando várias medianas, o cálculo depende se temos um valor numérico par ou ímpar.
Amplitude

A amplitude é então calculada como a diferença entre o máximo e o mínimo.
IQR

A amplitude interquartil é calculada como a diferença entre Q3 and Q1​.


