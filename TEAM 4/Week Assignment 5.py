import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# SAVE FIGURE: figure1.savefig(‘C:\My_folder\my_file_name.png’)

# PLOT GRAPHIC LINE: plt.plot(x_data,y_data); x_data = np.arange(4)

# PLOT GRAPHIC BAR: plt.bar(x,y)

# PLOT GRAPHIC PIE: plt.pie(sizes, autopct='%1, 1f%')

# PLOT GRAPHIC SCATTER: plt.scatter(x, y); x = np.random.rand(N)

df_covid_1 = pd.read_excel('COVID19_open_line_list.xlsx')

# df_covid_1['ID'].dropna()
# df_covid_1['date_confirmation'].dropna()
#
# RowNumber_i = 0
#
# while RowNumber_i < 13500:
#
#     Drop_i = df_covid_1.loc[df_covid_1.index == RowNumber_i, 'date_confirmation'].all()
#     if Drop_i == '':
#         df_covid_1.drop([RowNumber_i])
#
#     RowNumber_i = RowNumber_i + 1
#
# figure_covid_1 = plt.figure()
# # x_data = df_covid_1['date_confirmation']
# # y_data = df_covid_1['ID']
#
# df_covid_1.plot(df_covid_1['date_confirmation'], df_covid_1['ID'])
# plt.show()

# AGRUPANDO VALORES DE CASOS POR GÊNERO

# Inicializa a variável para começar da primeira linha da consulta
RowNumber_i = 1

#Percorre toda a tabela da linha 0 até a 13500
while RowNumber_i < 13500:
    Change_i = df_covid_1.loc[df_covid_1.index == RowNumber_i, 'sex'].all()
    if Change_i == 'Male':
        df_covid_1.loc[df_covid_1.index == RowNumber_i, 'sex'] = 'male'
    if Change_i == 'Female':
        df_covid_1.loc[df_covid_1.index == RowNumber_i, 'sex'] = 'female'

    RowNumber_i = RowNumber_i + 1

grouped_values = df_covid_1.groupby('sex').size()
print(grouped_values)
male_num = grouped_values.iloc[grouped_values.index == 'male'].values[0]
female_num = grouped_values.iloc[grouped_values.index == 'female'].values[0]

# Plotando o grafico de barras (COVID-19 Cases versus Gender)

figure_01 = plt.figure()
x = np.arange(2)
y = [male_num, female_num]
plt.bar(1, male_num, label='male')
plt.bar(2, female_num, label='female')
plt.legend(loc='upper right')
y_pos = np.arange(3)
sex = (0, 'male', 'female')
plt.xticks(y_pos, sex)
plt.show()




