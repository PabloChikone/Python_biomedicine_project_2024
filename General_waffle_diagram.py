import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pywaffle import Waffle


# создаем функцию, которая возвращающает список цветов, которые будем использовать в каждой визуализации
def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

def Function_General_waffle_diagram(start_name_file,  # путь к файлу с данными
                           data_excel,  # имя столбца из файла со значениями
                           name_excel,  # имя столбца из файла с названиями
                           name,  # имя диаграммы для подписи
                           final_file_address):  # путь с именем файла, куда сохраняем файл
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


    fig = plt.figure(FigureClass=Waffle,
                     rows=30,
                     columns=45,
                     values=list(df_s[data_excel]),
                     colors=pal_spec,
                     labels=[i+' '+format(j, ',') for i,j in zip(df_s[name_excel], df_s[data_excel])],
                     figsize = (15,6),
                     legend={'loc':'upper right',
                             'bbox_to_anchor': (1.32, 1)
                            })
    plt.tight_layout()

    # Добавляем подпись
    plt.figtext(0.34, 0.98, name, ha='center', fontsize=12)

    plt.savefig(final_file_address) # сохраняем файл

    plt.show() # показываем файл













