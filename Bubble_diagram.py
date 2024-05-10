import plotly.express as px
import pandas as pd

def Function_Bubble_diagram(data, x_col, y_col, size_col, hover_name_col, x_title, y_title, legend_title, title):
    """
    Создает пузырьковую диаграмму на основе переданных данных.

    Parameters:
    - data (DataFrame): Данные для визуализации.
    - x_col (str): Название столбца для оси x.
    - y_col (str): Название столбца для оси y.
    - size_col (str): Название столбца для размера пузырьков.
    - hover_name_col (str): Название столбца для всплывающих подсказок.
    - x_title (str): Заголовок оси x.
    - y_title (str): Заголовок оси y.
    - legend_title (str): Заголовок легенды.
    - title (str): Заголовок диаграммы.
    """

    # Создание пузырьковой диаграммы
    fig = px.scatter(data, x=x_col, y=y_col, size=size_col, hover_name=hover_name_col,
                     log_x=True, size_max=60, title=title)

    # Настройка меток осей и легенды
    fig.update_layout(xaxis_title=x_title, yaxis_title=y_title,
                      legend_title=legend_title,
                      legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                      showlegend=True)

    # Отображение диаграммы
    fig.show()