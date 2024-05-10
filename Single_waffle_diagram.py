import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pywaffle import Waffle

#создаем функцию, которая возвращающает список цветов, которые будем использовать в каждой визуализации
def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

def Function_Single_waffle_diagram(start_name_file, # путь к файлу с данными
                    data_excel, # имя столбца из файла со значениями
                    name_excel, # имя столбца из файла с названиями
                    name, # имя диаграммы для подписи
                    final_file_address, # путь с именем файла, куда сохраняем файл
                    percent_file_column): # имя столбца из файла с со значениями с долей процентов (должно соотв. data_excel)

    # Создаем DataFrame с данными для визуализации
    df = pd.read_excel(start_name_file)

    df_s = df.sort_values(by=data_excel, ascending=False)
    df_s.head(9)

    # создаем отсортированный DataFrame
    # df = df.sort_values(by=data_excel, ascending=False) #сортировка по убыванию
    # df = df.sort_values(by=data_excel, ascending=True) #сортировка по возрастанию

    # Создаем список цветов в переменных
    pal_vi = get_color('viridis_r', len(df))
    pal_plas = get_color('plasma_r', len(df))
    pal_spec = get_color('Spectral', len(df))
    pal_hsv = get_color('hsv', len(df))


    save_name = []
    for i,p,n,c in zip(df_s[data_excel], df_s[percent_file_column], df_s[name_excel], pal_spec):
        fig = plt.figure(FigureClass=Waffle,
                         rows=10, columns=20,
                         values=[i, sum(df_s[data_excel])-i],
                         colors=[c,'gainsboro'],
                         labels=[n + ' ' + str(round(p*100,1)) +' %','Другие значения'],
                         figsize = (8,8),
                         legend={'loc':'upper right', 'bbox_to_anchor': (1, 1), 'fontsize':24}
                        )
        save_name.append(final_file_address+'waffle_'+ n + '.svg')
        plt.tight_layout()
        plt.savefig(final_file_address+'waffle_'+ n + '.svg', bbox_inches='tight')   #сохраняем в файлы
        plt.show()