import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pywaffle import Waffle
from PIL import Image
import os

# Функция для создания коллажа
def create_collage(image_paths, rows, cols, output_path):
    # Открываем изображения
    images = [Image.open(path) for path in image_paths]
    # Определяем размеры каждого изображения
    width, height = images[0].size
    print(images)

    # Создаем новое изображение для коллажа
    collage_width = width * cols
    collage_height = height * rows
    collage = Image.new('RGB', (collage_width, collage_height))

    # Располагаем изображения на коллаже
    x_offset = 0
    y_offset = 0
    for img in images:
        collage.paste(img, (x_offset, y_offset))
        x_offset += width
        if x_offset == collage_width:
            x_offset = 0
            y_offset += height

    # Сохраняем коллаж
    collage.save(output_path)


#создаем функцию, которая возвращающает список цветов, которые будем использовать в каждой визуализации
def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

def Function_Multiple_waffle_diagram(start_name_file, # путь к файлу с данными
                    data_excel, # имя столбца из файла со значениями
                    name_excel, # имя столбца из файла с названиями
                    name, # имя диаграммы для подписи
                    final_file_address, # путь с именем файла, куда сохраняем файл
                    percent_file_column, # имя столбца из файла с со значениями с долей процентов (должно соотв. data_excel)
                    horizontal_grid_size, # размер горизонтальной сетки
                    vertical_grid_size):# размер вертикальной сетки

    # Создаем DataFrame с данными для визуализации
    df = pd.read_excel(start_name_file)

    # сортируем DataFrame
    df_s = df.sort_values(by=data_excel, ascending=False)
    df_s.head(9)

    # Создаем список цветов в переменных
    pal_vi = get_color('viridis_r', len(df))
    pal_plas = get_color('plasma_r', len(df))
    pal_spec = get_color('Spectral', len(df))
    pal_hsv = get_color('hsv', len(df))

    # создаем отдельные диаграммы
    save_name = []
    for idx, (i, p, n, c) in enumerate(zip(df_s[data_excel], df_s[percent_file_column], df_s[name_excel], pal_spec), start=1):
        fig = plt.figure(FigureClass=Waffle,
                         rows=30, columns=45,
                         values=[i, sum(df_s[data_excel])-i],
                         colors=[c,'gainsboro'],
                         labels=[n + ' ' + str(round(p*100,1)) +' %','Другие значения'],
                         figsize = (15,6),
                         legend={'loc':'upper right', 'bbox_to_anchor': (1, 1), 'fontsize':24}
                        )
        save_name.append(f'diagram\Диаграмма_{idx}.png')
        plt.tight_layout()
        plt.savefig(f'diagram\Диаграмма_{idx}.png', bbox_inches='tight')   #сохранение в файл
        #plt.show()

    image_paths = []

    # Обход файлов в указанной директории
    for file_name in os.listdir(final_file_address + r"\diagram"):
        # Проверяем, что файл имеет расширение SVG
        if file_name.endswith(".png"):
            # Получаем полный путь к файлу и добавляем его в список
            full_path = os.path.join(final_file_address + r"\diagram", file_name)
            image_paths.append(full_path)


    # Создание коллажа сеткой
    create_collage(image_paths, horizontal_grid_size, vertical_grid_size, r"Коллаж.png")
