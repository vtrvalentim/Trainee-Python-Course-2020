# AmBev - Trainee Supply 2020
# Weekly Assignment 4 - Team Supply Coders
# Raphael Eloi e Yago Nobre

#Importa a biblioteca de dataframes Pandas
import pandas as pd
import numpy as np

#Lê os arquivos .xlsx como dataframes
data_frame1 = pd.read_excel('Hyperbulk_input_v3.xlsx')
data_frame2 = pd.read_excel('SKU_dictionary.xlsx')

#Consolida as duas bases em uma única consulta
final_table = data_frame1.merge(data_frame2, left_on='ATOM编码', right_on='ABM EXPORT ID')

#Inicializa a variável para começar da primeira linha da consulta
RowNumber_i = 0

#Percorre toda a tabela da linha 0 até a 4044
while (RowNumber_i <= 4044):
    #Coleta as informações de Data e SKU de cada linha para somar Amount Sold e Total Revenue
    Date_i = final_table.loc[final_table.index == RowNumber_i, '日期'].values[0]
    SKU_Code_i = final_table.loc[final_table.index == RowNumber_i, 'ATOM编码'].values[0]
    #Soma se as datas forem compatíveis com Date_i e SKU for compatível com SKU_Code_i
    Amt_Sold_i = final_table.loc[(final_table['ATOM编码'] == SKU_Code_i) & (final_table['日期'] == Date_i), '零售金额 '].sum()
    Revenue_i = final_table.loc[(final_table['ATOM编码'] == SKU_Code_i) & (final_table['日期'] == Date_i), 'EXW (NR)'].sum()
    #Cria duas novas colunas escrevendo na linha respectiva os valores de Amount Sold e Total Revenue
    final_table.loc[final_table.index[RowNumber_i], 'Amt_Sold'] = Amt_Sold_i
    final_table.loc[final_table.index[RowNumber_i], 'Total Revenue'] = Revenue_i
    #Incremento de Linha
    RowNumber_i = RowNumber_i + 1

#Mostra a tabela final
print(final_table)
