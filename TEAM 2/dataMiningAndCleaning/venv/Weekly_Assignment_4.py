import numpy as np
import pandas as pd
from pandas import ExcelWriter

hyperbulk_data_frame = pd.read_excel('Hyperbulk_input_v3.xlsx')
sku_data_frame = pd.read_excel('SKU_dictionary.xlsx')

#print(hyperbulk_data_frame.columns)

hyperbulk_data_frame.columns = ['Date', 'Month', 'Channel', 'SKU number', 'SKU style', 'ATOM code', 'SKU Name', 'Year', 'Retail Amount', 'Type', 'Unnamed: 10']
print(hyperbulk_data_frame.columns)
print(sku_data_frame.columns)

hyperbulk_data_frame = hyperbulk_data_frame.drop(labels = ['Month','Channel','SKU number','SKU style','Year','Type','Unnamed: 10'], axis = 1)
sku_data_frame = sku_data_frame.drop(labels=['SKU Description','MoM ID','ABM UK ID','Alcohol Category','VILC','MACO','Margin %','TEST'], axis=1)
print(hyperbulk_data_frame.head(5))
print()
print(sku_data_frame.head(5))
print()

#print(hyperbulk_data_frame['ATOM code'])
#print(sku_data_frame['ABM EXPORT ID'])
final_table = hyperbulk_data_frame.merge(sku_data_frame,left_on='ATOM code',right_on='ABM EXPORT ID')
final_table = final_table.drop(labels=['ATOM code', 'ABM EXPORT ID'], axis=1)

print(final_table)

writer = ExcelWriter('PythonExport.xlsx')
final_table.to_excel(writer)
writer.save()