import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

def Function_Collage_Bar_graph_diagram(start_name_file,  # путь к файлу с данными
                                data_excel_1,  # имя столбца из файла со значениями 1
                                data_excel_2,  # имя столбца из файла со значениями 2
                                data_excel_3,  # имя столбца из файла со значениями 3
                                data_excel_4,  # имя столбца из файла со значениями 4
                                name_excel,  # имя столбца из файла с названиями
                                name,  # имя диаграммы для подписи
                                final_file_address):  # путь с именем файла, куда сохраняем файл
    # Создаем DataFrame с данными для визуализации
    df = pd.read_excel(start_name_file)

    # Список имен столбцов оси со значениями
    data_columns = [
        data_excel_1,
        data_excel_2,
        data_excel_3,
        data_excel_4,
    ]

    # Для цветовой гаммы
    try:
        pal_vi = sns.color_palette("viridis_r", n_colors=len(df)).as_hex()
    except:
        pal_vi = None

    # создаем коллаж
    fig = make_subplots(rows=2, cols=2, subplot_titles=data_columns)

    for i, column in enumerate(data_columns, start=1):
        row = math.ceil(i / 2)
        col = i % 2
        if col == 0:
            col = 2

        fig.add_trace(
            go.Bar(x=df[name_excel], y=df[column], text=df[column], name=column, marker_color=pal_vi[i - 1],
                   textposition='auto'),
            row=row, col=col
        )

    fig.update_traces(texttemplate='%{text:.3s}')

    fig.update_layout(
        title_text=name,
        height=800,
        width=1000,
        showlegend=False
    )

    fig.write_image(final_file_address)
    fig.show()