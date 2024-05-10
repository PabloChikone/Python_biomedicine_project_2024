import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# создаем функцию, которая возвращающает список цветов, которые будем использовать в каждой визуализации
def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

def Function_Radial_diagram(start_name_file, # путь к файлу с данными
                    data_excel, # имя столбца из файла со значениями
                    name_excel, # имя столбца из файла с названиями
                    name, # имя диаграммы для подписи
                    final_file_address):# путь с именем файла, куда сохраняем файл

    # Создаем DataFrame с данными для визуализации
    df = pd.read_excel(start_name_file)

    # создаем отсортированный DataFrame
    # df = df.sort_values(by=data_excel, ascending=False) #сортировка по убыванию
    # df = df.sort_values(by=data_excel, ascending=True) #сортировка по возрастанию


    # Устанавливаем стиль 'darkgrid'
    sns.set_style('darkgrid')

    # Создаем список цветов в переменных
    pal_vi = get_color('viridis_r', len(df))
    pal_plas = get_color('plasma_r', len(df))
    pal_spec = get_color('Spectral', len(df))
    pal_hsv = get_color('hsv', len(df))

    # установим размер фигуры
    plt.figure(figsize=(12,8))
    ax = plt.subplot(111, polar=True)
    sns.set_style('darkgrid')
    plt.axis()

    # Установим максимальное значение
    lowerLimit = 0
    max_v = df[data_excel].max()

    # Установим высоту и ширину
    heights = df[data_excel]
    width = 2*np.pi / len(df.index)

    # Установим индекс и угол
    indexes = list(range(1, len(df.index)+1))
    angles = [element * width for element in indexes]
    bars = ax.bar(x=angles, height=heights, width=width, bottom=lowerLimit,
              linewidth=1, edgecolor="white", color=pal_vi)
    labelPadding = 15

    # рисуем график
    for bar, angle, height, label, color in zip(bars, angles, heights, df[name_excel], pal_vi):
        rotation = np.rad2deg(angle)+20
        alignment = ""
        if angle >= np.pi / 2 and angle < 3 * np.pi / 2:
            alignment = "right"
            rotation = rotation + 180
        else:
            alignment = "left"
        ax.text(x=angle, y=lowerLimit + bar.get_height() + labelPadding,
                s=label, ha=alignment, va='center', rotation=rotation,
                rotation_mode="anchor", fontsize=8)

    # Добавим прямоугольник с цветом вручную
    ax.add_patch(plt.Rectangle((0, 0), 1, 1, color=color, label=label))

    # Добавим легенду
    ax.legend(loc="upper right")

    # Добавим подпись с названием графика
    ax.set_title(name, fontsize=12)

    # plt.xlabel('Ось X')
    # plt.ylabel('Ось Y')

    # размещаем легенду справа от графика
    plt.legend(bbox_to_anchor = (1, 1), loc = 2)
    plt.savefig(final_file_address)
    plt.show()