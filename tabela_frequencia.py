############################## BIBLIOTECAS ############################################
import numpy as np
import pandas as pd

#############################   TABELA    #############################################
tabela = pd.read_csv(r"digite o caminho da planilha aqui") # Passe o caminho da planilha dentro das aspas

col = tabela["digite a coluna aqui"].tolist() # Transforma coluna em lista

observando = list(set(col)) # Remove os valores duplicados / será usado como referência

k = len(observando) # Contar os elementos que se repetem

############################# FREQ. ABSOLUTA ##########################################
freq_abs = [col.count(observando[i]) for i in range(0, k)]

############################# FREQ. RELATIVA ##########################################
freq_rel = [round(col.count(observando[i]) / k, 4) for i in range(0, k)]


####################### FREQ. RELATIVA PERCENTUAL #####################################
freq_rel_per = [round((col.count(observando[i]) / k) * 100, 2) for i in range(0, k)]

####################### FREQ. ABSOLUTA AC #############################################
freq_abs_ac = list(np.cumsum(freq_abs))

####################### FREQ. RELATIVA PERCENTUAL AC ##################################
freq_rel_per_ac = list(np.cumsum(freq_rel_per))