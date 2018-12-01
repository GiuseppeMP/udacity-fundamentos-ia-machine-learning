# import normal
import math
import datetime

#import com alias
import multiprocessing as mp

#import somente de um pedaço da biblioteca
from csv import reader as csvreader

## o que não fazer, os nomes importados podem ser sobreescritos
from random import *


'''Nossos módulos favoritos
A biblioteca padrão do Python tem vários módulos! Para ajudar você a se familiarizar com o que está disponível, aqui está uma seleção de nossos módulos favoritos da biblioteca padrão do Python e por que os usamos!

csv: muito conveniente para ler e gravar arquivos csv
collections: extensões úteis dos tipos comuns de dados, incluindo OrderedDict, defaultdict e namedtuple
random: gera números pseudoaleatórios, mistura sequências aleatoriamente e seleciona itens de maneira aleatória
string: mais funções para strings. Este módulo também contém coleções úteis de letras como string.digits (uma string que contém todos os caracteres que são dígitos válidos).
re: correspondência de padrões em strings através de expressões regulares
math: algumas funções matemáticas padrão
os: interagindo com sistemas operacionais
os.path: submódulo de os para alterar o nome de caminhos
sys: trabalha diretamente com o interpretador do Python
json: bom para ler e escrever arquivos json (bom para trabalhos na web)
Esperamos que você os ache úteis!'''

print(math.pow(2,3))
print(datetime.datetime.today())
print(mp.cpu_count())
