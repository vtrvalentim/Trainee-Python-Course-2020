import pandas as pd
import numpy as np


# importar os arquivos
historico_vendas = pd.read_excel(r'inputs\Hyperbulk_input_v3.xlsx')
dicionario_sku = pd.read_excel('inputs\\SKU_dictionary.xlsx')

#_______________________________________________________________________________________________________________________
# limpar dados
# renomear colunas
historico_vendas.columns = ['Data', 'lixo1', 'lixo2', 'lixo3', 'lixo4', 'ID_merge',
       'SKU Name', 'lixo5', 'lixo6 ', 'lixo7', 'lixo8']
dicionario_sku.columns = ['lixo1', 'lixo2', 'lixo3', 'ID_merge_dict',
       'lixo4', 'Net_Revenue', 'lixo5', 'lixo6', 'lixo7', 'lixo8']

# remover colunas lixo
historico_vendas_limpo = historico_vendas[['ID_merge','Data','SKU Name']]
dicionario_sku_limpo = dicionario_sku[['ID_merge_dict','Net_Revenue']]

#_______________________________________________________________________________________________________________________
# juntar as tabelas
tabela_junta = pd.merge(historico_vendas_limpo,
                        dicionario_sku_limpo,
                        left_on='ID_merge',
                        right_on='ID_merge_dict',
                        how='left')

tabela_junta_limpa = tabela_junta[['Data','SKU Name','Net_Revenue']]
#_______________________________________________________________________________________________________________________
# agregar os dados por SKU Name e Data

#amount sold
tabela_junta_limpa_semrev = tabela_junta_limpa[['Data','SKU Name']]
# Create empty column
count = pd.Series(1,index=tabela_junta_limpa_semrev.index)
# Insert batch column into reordered_clean_table
tabela_junta_limpa_semrev.insert(2,'Amount_sold',count)

# pra cada par data e sku name conte quantas instancias
quantidade_vendida = tabela_junta_limpa_semrev.groupby(by=['Data','SKU Name'])["Amount_sold"].count().reset_index(name="count")

#print(quantidade_vendida.columns)

# Total revenue
# pra cada par data e sku name conte quantas instancias
total_revenue = tabela_junta_limpa.groupby(by=['Data','SKU Name'])["Net_Revenue"].sum().reset_index(name="Total_Revenue")
#print(quantidade_vendida.columns)

#merge tables
tabela_final_junta = pd.merge(quantidade_vendida,
                        total_revenue,
                        how='left')

#print(tabela_final_junta.head(10))
#_______________________________________________________________________________________________________________________
# exportar output

tabela_final_junta.to_excel('Export_analise.xlsx')