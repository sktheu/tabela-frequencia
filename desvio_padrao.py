# -*- coding: utf-8 -*-
"""DesvioPadrao(Atualizado).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15qQxr8hBWHxuser4rghVZzsDUMDKL90b
"""

import numpy as np
import pandas as pd
from prettytable import PrettyTable

x1 = pd.read_csv(r"dados.csv",delimiter=";")

## transformando uma coluna em lista
xi = x1['dados'].tolist()
#xi = [1,2,3,4,5]

# 
n = len(xi)

# transformar os dados em lista
obs = list(set(xi))

# numero de dados observados
k = len(obs)

# lista de frquencia absoluta
ni = [xi.count(obs[i]) for i in range(0,k)]
#ni = [142,165,163,167,163]

## coluna para calculo da media

xini = [obs[i]*ni[i] for i in range(0,k)]


## calculo da media
xmed = sum(xini)/sum(ni)


## coluna da variancia
colvar = [round((obs[i]-xmed)**2*ni[i],4) for i in range(0,k)]


## calculo variancia
var = round(sum(colvar)/sum(ni),4)
print (var)

## tabela de calculos

Tabela = PrettyTable()

Tabela.add_column("Dados", obs)
Tabela.add_column("Fa", ni)
Tabela.add_column("xini", xini)
Tabela.add_column("var", colvar)

Tabela.add_row(["Total", sum(ni), sum(xini), round(sum(colvar),4)])
print(Tabela)