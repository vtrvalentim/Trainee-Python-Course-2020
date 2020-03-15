import pandas as pd
import numpy as np

#LER O NOME DAS COLUNAS

#data_frame = pd.read_excel('Hyperbulk_input_v3.xlsx')
#print(data_frame.columns)

data_frame1 = pd.read_excel('Hyperbulk_input_v3.xlsx')

data_frame2 = pd.read_excel('SKU_dictionary.xlsx')

#Data = data_frame1['日期']
#data_frame1.insert(0, column='Date', value=Data)

#SKU_Name = data_frame1['SKU Name']
#data_frame1.insert(1, column='SKU_Name', value=SKU_Name)

#Amt_Sold = data_frame1['零售金额 ']
#data_frame1.insert(2, column='Amt_Sold', value=Amt_Sold)

#Total_EXW = (data_frame2['EXW (NR)']*data_frame1['零售金额 '])
#data_frame2.insert(3, column='Total_EXW', value=Total_EXW)

#falta somar a quantidade total vendida por dia e tirar o net revenue disso diário

final_table = data_frame1.merge(data_frame2, left_on='ATOM编码', right_on='ABM EXPORT ID')

#print(final_table)
#coluna data = 日期

RowNumber_i = 0

while (RowNumber_i <= 4044):
    Date_i = final_table.loc[final_table.index == RowNumber_i, '日期'].values[0]
    SKU_Code_i = final_table.loc[final_table.index == RowNumber_i, 'ATOM编码'].values[0]
    Amt_Sold_i = final_table.loc[(final_table['ATOM编码'] == SKU_Code_i) & (final_table['日期'] == Date_i), '零售金额 '].sum()
    final_table.loc[final_table.index[RowNumber_i], 'Amt_Sold'] = Amt_Sold_i

    RowNumber_i = RowNumber_i + 1


#print(final_table.head(10))
print(final_table['ATOM编码'].head(10))
print(final_table['日期'].head(10))
print(final_table['Amt_Sold'].head(10))


#print(final_table[final_table['Date'] == '2019-08-09'])
