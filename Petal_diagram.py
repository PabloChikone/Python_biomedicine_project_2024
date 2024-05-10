import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def Function_Petal_diagram(start_name_file, # путь к файлу с данными
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

    # Уменьшим количество цветов, чтобы избежать ошибки
    pal_vi = get_color('viridis_r', min(5, len(df)))

    fig = px.line_polar(df, r=data_excel,
                        theta=name_excel, line_close=True)
    fig.update_traces(fill='toself', line=dict(color=pal_vi[2]))

    # Добавляем названия осей и название диаграммы
    fig.update_layout(
        title=name
    )

    # Сохраняем изображение в файл
    fig.write_image(final_file_address)

    fig.show()