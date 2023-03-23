# -*- coding: utf-8 -*-
"""MediaIntervalo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mkhc1aZi8wx4Hti0Z06yS9aa1NgMVtCd
"""

### BIBLIOTECAS ↓↓↓↓
import numpy as np
import pandas as pd
import math
from prettytable import PrettyTable

#dados_brutos = pd.read_excel("INSIRA O NOME.xlsx")  #USE ESSE CASO O FORMATO FOR EXCEL
dados_brutos = pd.read_csv(r"dados.csv") 

### Transformando uma coluna em lista
X = dados_brutos['dados'].tolist()

### CONSTRUÇÃO DOS INTERVALOS DE CLASSES ↓↓↓↓

### Número de elementos
n = len(X)

### Número de linhas
k = math.ceil(math.log10(n) * 3.3 + 1)    #USE ESSE CASO O TOTAL DE ELEMENTOS FOR MAIOR QUE 40
# k = math.ceil(math.sqrt(n)) 

### Amplitude total
AT = max(X) - min(X)

### Amplitude da classe
h = math.ceil(AT / k) #USE ESSE, CASO FOR PELO MÉTODO DE SURGES
#h = math.ceil(AT / k) + 1

### LISTA DOS LIMITES ↓↓↓↓
L = [min(X) + i * h for i in range(0, k + 1)]

### Limites inferiores
li = L[0:k]

### Limites superiores
ls = L[1:(k+1)]
classes = [str(li[i]) + str('|---') + str(ls[i]) for i in range(0, k)]

### Ponto Médio 
xi = [(li[i] + ls[i]) / 2 for i in range(0, k)]

### Ordenar lista
X.sort()

### Transformar X em Serie
Xserie = pd.Series(X)

### Frequência Absoluta
freq_abs = pd.cut(Xserie, bins=L, right=False, include_lowest=True).value_counts(sort=False)

### MÉDIA ↓↓↓↓

### Ni
ni = list(freq_abs)

### Xi.Ni
xini = [xi[i] * ni[i] for i in range(0, k)]

### Numerador da fórmula da média
NUM = sum(xini)

### Resultado da Média
xmed = NUM / n
xmed

### MONTANDO A TABELA ↓↓↓↓