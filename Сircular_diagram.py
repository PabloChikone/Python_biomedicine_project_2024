import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def Function_Сircular_diagram(start_name_file, # путь к файлу с данными
                    data_excel, # имя столбца из файла со значениями
                    name_excel, # имя столбца из файла с названиями
                    name, # имя диаграммы для подписи
                    final_file_address):# путь с именем файла, куда сохраняем файл

    # Создаем DataFrame с данными для визуализации
    df = pd.read_excel(start_name_file)
    # создаем отсортированный DataFrame
    # df = df.sort_values(by=data_excel, ascending=False) #сортировка по убыванию
    # df = df.sort_values(by=data_excel, ascending=True) #сортировка по возрастанию

    #создаем функцию, которая возвращающает список цветов, которые будем использовать в каждой визуализации
    def get_color(name, number):
        pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
        return pal

    # Создаем список цветов в переменных
    pal_vi = get_color('viridis_r', len(df))
    pal_plas = get_color('plasma_r', len(df))
    pal_spec = get_color('Spectral', len(df))
    pal_hsv = get_color('hsv', len(df))

    # установим размер фигуры
    plt.gcf().set_size_inches(12, 8)
    sns.set_style('darkgrid')

    # Установим максимальное значение
    max_val = max(df[data_excel])*1.01
    ax = plt.subplot(projection='polar')

    # Зададим внутренний график
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(1)
    ax.set_rlabel_position(0)
    ax.set_thetagrids([], labels=[])
    ax.set_rgrids(range(len(df)), labels= df[name_excel])

    # Установим график с полярной проекцией
    ax = plt.subplot(projection='polar')
    for i in range(len(df)):
        ax.barh(i, list(df[data_excel])[i]*2*np.pi/max_val,
                label=list(df[name_excel])[i], color=pal_plas[i])

    # Уменьшим размер шрифта подписей
    ax.set_rgrids(range(len(df)), labels=df[name_excel], fontsize=6)

    # Добавим подпись с названием графика
    ax.set_title(name, fontsize=12)

    # plt.xlabel('Ось X')
    # plt.ylabel('Ось Y')

    # размещаем легенду справа от графика
    plt.legend(bbox_to_anchor = (1, 1), loc = 2)
    plt.savefig(final_file_address)
    plt.show()