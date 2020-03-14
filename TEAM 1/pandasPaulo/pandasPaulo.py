
import pandas as pd
import numpy as np

#IMPORTANDO PLANILHAS#

data_hyperbulk = pd.read_excel("F:\Paulo\Documents\GitHub\Trainee-Python-Course-2020\TEAM 1\pandasPaulo\Hyperbulk_input_v3.xlsx")
data_sku_dic = pd.read_excel("F:\Paulo\Documents\GitHub\Trainee-Python-Course-2020\TEAM 1\pandasPaulo\SKU_dictionary.xlsx")

# #VERIFICANDO CONTEUDO DAS COLUNAS
# Teste
# print(data_hyperbulk.columns)
# print(data_sku_dic.columns)
#
# Index(['日期', '月份 Month', '渠道 Channel', 'SKU 编号', '款式 SKU', 'ATOM编码',
#        'SKU Name', '年份 Age', '零售金额 ', '类型', 'Unnamed: 10'],
#       dtype='object')
# Index(['SKU Description', 'MoM ID', 'ABM UK ID', 'ABM EXPORT ID',
#        'Alcohol Category', 'EXW (NR)', 'VILC', 'MACO', 'Margin %', 'TEST'],
#       dtype='object')

vendas_aux = data_hyperbulk[['日期', 'ATOM编码', 'SKU Name']]
vendas_aux = vendas_aux.rename(columns= {'日期':'Date','ATOM编码':'SKU_ID','SKU Name':'SKU_Name'})

SKU_aux = data_sku_dic[['ABM EXPORT ID', 'EXW (NR)']]
SKU_aux = SKU_aux.rename(columns= {'ABM EXPORT ID':'SKU_ID','EXW (NR)':'EXW'})

#Criando a coluna chave para fazer a contagem de linhas em que aparece uma combinação data-sku

vendas_aux['Chave'] = vendas_aux.Date.astype(str).str.cat(vendas_aux.SKU_ID.astype(str), sep='_')

vendas_aux['Chave'] = vendas_aux.Chave.astype(str).str.cat(vendas_aux.SKU_Name.astype(str), sep='_')

# print(vendas_aux)

#contagem das linhas

qtd_vendida = vendas_aux.pivot_table(index=['Chave'], aggfunc='size')

qtd_vendida.columns = ['Chave', 'QTD_VENDIDA']

#print(qtd_vendida.columns)

#tab_final = qtd_vendida.merge(vendas_aux,left_on= 'Chave', right_on= 'Chave')



# chave = vendas_aux['Date']
# chave.columns = ['Chave']
# # print(chave.columns)
# copia_aux = vendas_aux['SKU ID'].copy()
#
# chave['Chave'] = chave['Chave'].str.cat(copia_aux,sep="_")




