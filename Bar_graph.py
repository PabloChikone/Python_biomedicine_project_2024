import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

def Function_Bar_graph_diagram(start_name_file, # путь к файлу с данными
                    data_excel, # имя столбца из файла со значениями
                    name_excel, # имя столбца из файла с названиями
                    name, # имя диаграммы для подписи
                    final_file_address):# путь с именем файла, куда сохраняем файл
    # Создаем DataFrame с данными для визуализации
    df = pd.read_excel(start_name_file)
    #задаем цвета
    pal_vi = get_color('viridis_r', len(df))
    # строим гистограмму
    fig = px.bar(df, x=name_excel, y=data_excel, text=data_excel,
                 color =name_excel, color_discrete_sequence=pal_vi)

    fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
    fig.update_layout({'plot_bgcolor': 'white',
                       'paper_bgcolor': 'white',
                       'title': {'text': name, 'y':0.997}})  # Добавляем описание графика и сдвигаем его немного вниз

    # центрируем
    fig.update_layout(width=1100, height=500,
                      margin = dict(t=15, l=15, r=15, b=15))
    # выводим
    plt.savefig(final_file_address)
    fig.show()
