import pandas as pd
import  numpy as np

# Importing .csv data to data_frames
sku_dict = pd.read_excel('SKU_dictionary.xlsx')
hb_data = pd.read_excel('Hyperbulk_input_v3.xlsx', dtype= {'ATOM编码': object}, skip_blank_lines = True)

# Required columns: Date (hb_data - 日期), SKU Name ( sku_dict - SKU Description),
# Amt Sold (hb_data - 零售金额 ), Total EXW (sku_dict - EXW (NR))
# ------ key: hb_data - ATOM编码 > sku_dict - ABM EXPORT ID

aux_hb = hb_data[['ATOM编码', '日期','零售金额 ']]
aux_sku = sku_dict[['ABM EXPORT ID', 'SKU Description']]

compiled_table = aux_sku.merge(aux_hb,left_on = 'ABM EXPORT ID', right_on = 'ATOM编码')
compiled_table = compiled_table.rename(columns= {'SKU Description':'SKU','零售金额 ':'Amt Sold','日期':'Date'})
compiled_table =compiled_table.drop(axis=1, labels='ATOM编码')

compiled_table.to_excel('compiled_table.xls')

print(compiled_table)
