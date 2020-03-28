import pandas as pd
import  numpy as np

# Importing .csv data to data_frames
sku_dict = pd.read_excel('SKU_dictionary.xlsx')
hb_data = pd.read_excel('Hyperbulk_input_v3.xlsx', dtype= {'ATOM编码': object}, skip_blank_lines = True)

# Required columns: Date (hb_data - 日期), SKU Name ( sku_dict - SKU Description),
# Amt Sold (hb_data - 零售金额 ), Total EXW (sku_dict - EXW (NR))
# ------ key: hb_data - ATOM编码 > sku_dict - ABM EXPORT ID

aux_hb = hb_data[['ATOM编码', '日期']]
aux_sku = sku_dict[['ABM EXPORT ID', 'SKU Description', 'EXW (NR)']]

compiled_table = aux_sku.merge(aux_hb,left_on = 'ABM EXPORT ID', right_on = 'ATOM编码')
compiled_table = compiled_table.rename(columns= {'ABM EXPORT ID':'ID', 'SKU Description':'SKU','EXW (NR)':'EXW','日期':'Date'})
compiled_table = compiled_table.drop(axis=1, labels='ATOM编码')

teste = compiled_table.iloc[0]['EXW']
print(type(teste),teste)

count_table = compiled_table.pivot_table(values= 'EXW', index=['Date', 'ID', 'SKU'], aggfunc= ('size', np.sum))


count_table = count_table.rename(columns= {'size':'Units sold', 'sum':'Total EXW'})

count_table.to_excel('processed_table.xls')