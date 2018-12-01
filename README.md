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

## Aula 3: Lecture 03. Dias úteis x fins de semana - qual a diferença?

É  possível observar que o número de cães é igual durante a semana e no fins de semana mas a propagação varia.