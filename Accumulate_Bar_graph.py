import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

def Function_Accumulate_Bar_graph_diagram(start_name_file, # путь к файлу с данными
                    data_excel_1, # имя столбца из файла со значениями 1 варианта данных
                    data_excel_2, # имя столбца из файла со значениями 2 варианта данных
                    name_excel, # имя столбца из файла с названиями
                    name, # имя диаграммы для подписи
                    final_file_address): # путь с именем файла, куда сохраняем файл


    # Создаем DataFrame с данными для визуализации
    df = pd.read_excel(start_name_file)
    #emd_excel = "Ошибочные ЭМД"

    # Извлекаем данные из DataFrame
    data1 = df[data_excel_1]
    data2 = df[data_excel_2]
    names = df[name_excel]

    # Создаем бины для гистограммы
    bins = range(len(names))

    # Устанавливаем размер фигуры
    plt.figure(figsize=(16, 8))  # делаем более высокое расширение картинки

    # Получаем цветовую палитру
    pal_vi = get_color('viridis_r', len(df))
    pal_plas = get_color('plasma_r', len(df))
    pal_spec = get_color('Spectral', len(df))
    pal_hsv = get_color('hsv', len(df))

    # Рисуем накопительную гистограмму с использованием палитры цветов
    plt.bar(names, data1, color=pal_vi, label=data_excel_1)
    plt.bar(names, data2, bottom=data1, color=pal_hsv, label=data_excel_2)

    # Настраиваем оси и метки
    plt.xlabel(name_excel)
    plt.ylabel("Количество, ед.")
    plt.title(name)
    #plt.legend("12")

    # Отображаем график и сохраняем его
    plt.savefig(final_file_address, dpi=1500)
    plt.show()