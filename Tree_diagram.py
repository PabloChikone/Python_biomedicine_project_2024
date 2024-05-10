import pandas as pd
import plotly.express as px
import numpy as np

# функция построения древовидной диаграммы
def Function_Tree_diagram(start_name_file, # путь к файлу с данными
                    data_excel, # имя столбца из файла со значениями
                    name_excel, # имя столбца из файла с названиями
                    name, # имя диаграммы для подписи
                    final_file_address):# путь с именем файла, куда сохраняем файл

    # Создаем DataFrame с данными для визуализации
    df = pd.read_excel(start_name_file)

    # Исключаем строки с нулевыми значениями
    df_filtered = df[df[data_excel] != 0]

    # Вычисляем максимальное значение для диаграммы
    max_value_df_filtered = df_filtered[data_excel].max()

    # Строим диаграмму
    fig = px.treemap(df_filtered, path=[px.Constant(name_excel), name_excel],
                     values=df_filtered[data_excel],
                     color=df_filtered[data_excel],
                     color_continuous_scale='rdylgn',
                     color_continuous_midpoint=np.average(df_filtered[data_excel]),
                     range_color = [0, max_value_df_filtered]
                    )
    # Добавляем название диаграммы
    fig.update_layout(title=name)

    # Обновляем текстовую информацию на диаграмме
    fig.update_traces(textinfo="label+value+percent entry")

    # задаем размеры графика в окне
    fig.update_layout(margin = dict(t=100, l=25, r=25, b=25))

    # Сохраняем диаграмму в SVG файл
    fig.write_image(final_file_address)

    # выводим диаграмму в окно браузера
    fig.show()