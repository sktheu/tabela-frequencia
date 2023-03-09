############################## BIBLIOTECAS ############################################
import numpy as np
import pandas as pd
from prettytable import PrettyTable

#############################   TABELA    #############################################
x1 = pd.read_csv(r"digite o nome do arquivo .csv") # Passe o caminho da planilha dentro das aspas

X = x1["digite a coluna aqui"].tolist() # Transforma coluna em lista

# Total
n = len(X)

obs = list(set(X)) # Remove os valores duplicados / será usado como referência

k = len(obs) # Contar os elementos que se repetem

############################# FREQ. ABSOLUTA ##########################################
freq_abs = [X.count(obs[i]) for i in range(0, k)]

############################# FREQ. RELATIVA ##########################################
freq_rel = [round(X.count(obs[i]) / n, 4) for i in range(0, k)]


####################### FREQ. RELATIVA PERCENTUAL #####################################
freq_rel_per = [round((X.count(obs[i]) / n) * 100, 2) for i in range(0, k)]

####################### FREQ. ABSOLUTA AC #############################################
freq_abs_ac = list(np.cumsum(freq_abs))

####################### FREQ. RELATIVA PERCENTUAL AC ##################################
freq_rel_per_ac = list(np.cumsum(freq_rel_per))


####################### TABELA DE FREQUÊNCIAS #########################################
tabela_freqs = PrettyTable()
tabela_freqs.add_column("Dados", obs)
tabela_freqs.add_column("FA", freq_abs)
tabela_freqs.add_column("FR", freq_rel)
tabela_freqs.add_column("FR%", freq_rel_per)
tabela_freqs.add_column("FAC", freq_abs_ac)
tabela_freqs.add_column("FAR%", freq_rel_per_ac)

tabela_freqs.add_row(["Total:", sum(freq_abs), sum(freq_rel), sum(freq_rel_per), "-", "-"])
print(tabela_freqs)