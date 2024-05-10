import math
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

# даем ссылки на файлы с функциями
from Tree_diagram import Function_Tree_diagram
from Сircular_diagram import Function_Сircular_diagram
from Radial_diagram import Function_Radial_diagram
from General_waffle_diagram import Function_General_waffle_diagram
from Single_waffle_diagram import Function_Single_waffle_diagram
from Multiple_waffle_diagram import Function_Multiple_waffle_diagram
from Petal_diagram import Function_Petal_diagram
from Bar_graph import Function_Bar_graph_diagram
from Accumulate_Bar_graph import Function_Accumulate_Bar_graph_diagram
from Collage_Bar_graph import Function_Collage_Bar_graph_diagram
from Sector_diagram import Function_Sector_diagram
from Bubble_diagram import Function_Bubble_diagram

from Diagnosis import read_csv
from Diagnosis import read_excel
from Diagnosis import write_csv
from Diagnosis import write_excel
from Diagnosis import unique_values_column
from Diagnosis import count_and_merge_data
from Diagnosis import data_unique_column_append
from Diagnosis import filter_data_append
from Diagnosis import data_unique_column_append_age
from Diagnosis import format_excel_file


# Путь к файлу с исходными данными
start_name_file = r"D:\Python\pythonProject1_1Med\тест\Ошибки.xlsx"
# имя столбца со значениями
data_file_column = "за 2023 год"
# имя столбца с названиями
name_file_column = "Вид ошибки"
# название графика
name_diagramm = "График ..."
# название итогового файла
final_name_file = r"D:\Python\pythonProject1_1Med\diagram.svg"

# Пример использования древодидной диаграммы
#Function_Tree_diagram(start_name_file, data_file_column, name_file_column, name_diagramm, final_name_file)

# Пример использования круговой диаграммы
#Function_Сircular_diagram(start_name_file, data_file_column, name_file_column, name_diagramm, final_name_file)

# Пример использования радиальной диаграммы
#Function_Radial_diagram(start_name_file, data_file_column, name_file_column, name_diagramm, final_name_file)

# Пример использования общей вафельной диаграммы
#Function_General_waffle_diagram(start_name_file, data_file_column, name_file_column, name_diagramm, final_name_file)

# Пример использования одиночной вафельной диаграммы
# имя столбца с процентами для фрагмента диаграммы
#percent_file_column = "процент 2023"
#Function_Single_waffle_diagram(start_name_file, data_file_column, name_file_column, name_diagramm, final_name_file, percent_file_column)

# Пример использования нескольких одиночных вафельных диаграмм (коллаж)
#percent_file_column = "процент 2023"
#Function_Multiple_waffle_diagram(start_name_file, data_file_column, name_file_column, name_diagramm, final_name_file,
#                                 percent_file_column,2,2)

# Пример использования лепестковой диаграммы
#Function_Petal_diagram(start_name_file, data_file_column, name_file_column, name_diagramm, final_name_file)

# Пример использования гистограммы
#Function_Bar_graph_diagram(start_name_file, data_file_column, name_file_column, name_diagramm, final_name_file)

# Пример использования накопительной гистограммы для 2-х градаций
#data_file_column_1 = "за 2022 год"
#data_file_column_2 = "за 2023 год"
#Function_Accumulate_Bar_graph_diagram(start_name_file, data_file_column_1, data_file_column_2, name_file_column, name_diagramm, final_name_file)

# Пример использования коллажа из гистограмм 2х2
#data_file_column_1 = "за 2020 год"
#data_file_column_2 = "за 2021 год"
#data_file_column_3 = "за 2022 год"
#data_file_column_4 = "за 2023 год"
#Function_Collage_Bar_graph_diagram(start_name_file, data_file_column_1, data_file_column_2,
#                                    data_file_column_3, data_file_column_4, name_file_column, name_diagramm, final_name_file)

# Пример секторной диаграммы
#Function_Sector_diagram(start_name_file, data_file_column, name_file_column, name_diagramm, final_name_file)

# Пример пузырьковой диаграммы (для трехмерных данных)
"""
data = {
    "Country": ["USA", "China", "India", "Brazil", "Russia"],
    "Population": [331, 1440, 1380, 213, 146],
    "GDP": [21427, 14342, 2945, 1839, 1656],  # В миллиардах долларов
    "Area": [9.8, 9.6, 3.3, 8.5, 17.1]  # В миллионах квадратных километров
}
df = pd.DataFrame(data) #Данные для визуализации
x_col = "Population" #Название столбца для оси x - должно равняться названию столбца
y_col = "GDP" #Название столбца для оси y - должно равняться названию столбца
size_col = "Area" #Название столбца для размера пузырьков - должно равняться названию столбца
hover_name_col = "Country" #Название столбца для всплывающих подсказок- должно равняться названию столбца
x_title = "..." #Заголовок оси x
y_title = "..." #Заголовок оси y
legend_title = "..." #Заголовок легенды
title = "..." #Заголовок диаграммы
Function_Bubble_diagram(df, x_col, y_col, size_col, hover_name_col, x_title, y_title, legend_title, title)
"""

# Пример постобработки исходного csv файла
"""
id_patient
case_patient_gender_ru
case_patient_birthdate
diagnosis_mkb_code4
case_fiemk_date
"""
# формируем дата фрейм с исходными данными
data = read_csv(r"D:\Python\pythonProject1_1Med\Анализ болезней кровообращения\Сведения о случаях заболеваниях кровообращения 2019-2024.csv")

# удаляем дубликаты
data_unique = data.drop_duplicates()

# приводим в порядок столбец с датой case_fiemk_date
data_unique = data_unique[data_unique['case_fiemk_date'] != 'case_fiemk_date']
data_unique['case_fiemk_date'] = pd.to_datetime(data_unique['case_fiemk_date'])
data_unique['case_fiemk_date'] = data_unique['case_fiemk_date'].dt.strftime('%d.%m.%Y')

# приводим в порядок столбец с датой case_patient_birthdate
data_unique = data_unique[data_unique['case_patient_birthdate'] != 'case_patient_birthdate']
data_unique['case_patient_birthdate'] = pd.to_datetime(data_unique['case_patient_birthdate'])
data_unique['case_patient_birthdate'] = data_unique['case_patient_birthdate'].dt.strftime('%d.%m.%Y')

# расширяем датафрейм столбцом с группировкой по диагнозам
data_mkb_code = read_excel(r"D:\Python\pythonProject1_1Med\Анализ болезней кровообращения\МБК_кровообращения.xlsx")
data_append = data_unique_column_append(data_unique, data_mkb_code, "diagnosis_mkb_code4")
# + добавляем сюда же столбец с возрастом пациента в годах
data_append = data_unique_column_append_age(data_append, "case_patient_birthdate")


# далее расчитаем по data_append количество заболеваний по фильтрам
data_filter = read_excel(r"D:\Python\pythonProject1_1Med\Анализ болезней кровообращения\Расчет по болезням.xlsx")
data_merge = filter_data_append(data_filter, data_append)

write_excel(data_merge, r"D:\Python\pythonProject1_1Med\Анализ болезней кровообращения\Расчет по болезням_итог.xlsx")
# форматирование эксель для красоты
format_excel_file(r"D:\Python\pythonProject1_1Med\Анализ болезней кровообращения\Расчет по болезням_итог.xlsx")


# вафельная диаграмма
start_name_file_ = r"D:\Python\pythonProject1_1Med\Анализ болезней кровообращения\Расчет по болезням_итог.xlsx"
# имя столбца со значениями
data_file_column_ = "Количество случаев заболевания в 2023"
# имя столбца с названиями
name_file_column_ = "Наименование группы болезни"
# название графика
name_diagramm_ = "График ..."
# название итогового файла
final_name_file_ = r"D:\Python\pythonProject1_1Med\diagram.svg"
Function_General_waffle_diagram(start_name_file_, data_file_column_, name_file_column_, name_diagramm_, final_name_file_)







# формируем файл по подсчету количества значений по столбцу
# data_merge = count_and_merge_data(data_unique_column, "diagnosis_mkb_code4",
#                                   data, "diagnosis_mkb_code4")

# получаем датафрейм с уникальными значениями столбцов
# data_unique_column = unique_values_column(data_unique)

# запись в итоговый файл
# write_excel(data_merge, r"D:\Python\pythonProject1_1Med\Анализ болезней кровообращения\мерже.xlsx")
write_csv(data_append, r"D:\Python\pythonProject1_1Med\Анализ болезней кровообращения\тест.csv")


#