import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def Function_Sector_diagram(start_name_file, # путь к файлу с данными
                    data_excel, # имя столбца из файла со значениями
                    name_excel, # имя столбца из файла с названиями
                    name, # имя диаграммы для подписи
                    final_file_address):# путь с именем файла, куда сохраняем файл

    # Создаем DataFrame с данными для визуализации
    df = pd.read_excel(start_name_file)


    df_s = df.sort_values(by=data_excel, ascending=False)
    df_s.head(9)

    def get_color(name, number):
        pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
        return pal

    pal_vi = get_color('viridis_r', len(df))

    fig = px.pie(df_s, values=data_excel, names=name_excel,
                 color =name_excel, color_discrete_sequence=pal_vi)
    fig.update_traces(textposition='inside',
                      textinfo='percent+label',
                      sort=False)
    fig.update_layout(width=1000, height=550,
                      title=name)  # Добавляем название диаграммы

    fig.write_image(final_file_address)  # Сохраняем изображение в файл
    fig.show()
