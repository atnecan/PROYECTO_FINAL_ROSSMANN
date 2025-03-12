# eda.py

import logging
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def initial_eda(df: pd.DataFrame):
    """
    Exploración inicial de los datos (antes de la limpieza).
    Muestra head, info, describe y un histograma de ventas.
    """
    logging.info("Iniciando EDA inicial...")

    print("\n--- HEAD ---")
    print(df.head())

    print("\n--- INFO ---")
    print(df.info())

    print("\n--- DESCRIBE ---")
    print(df.describe())

    # Histograma de ventas
    if 'Sales' in df.columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(df['Sales'], kde=True)
        plt.title('Distribución de Ventas (Inicial)')
        plt.show()

    logging.info("EDA inicial completado.")

def final_eda(df: pd.DataFrame):
    """
    Exploración tras la limpieza:
    - Mapa de calor de correlaciones (columnas numéricas).
    - Gráfico de tendencia de ventas en el tiempo.
    """
    logging.info("Iniciando EDA final...")

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 1:
        plt.figure(figsize=(10, 8))
        sns.heatmap(df[numeric_cols].corr(), annot=True, fmt=".2f", cmap='coolwarm')
        plt.title("Mapa de Calor de Correlaciones (Post-Limpieza)")
        plt.show()

    if 'Date' in df.columns and 'Sales' in df.columns and df['Date'].isnull().sum() == 0:
        df_sorted = df.sort_values(by='Date')
        plt.figure(figsize=(12, 5))
        plt.plot(df_sorted['Date'], df_sorted['Sales'], alpha=0.5)
        plt.title("Ventas a lo largo del tiempo (Post-Limpieza)")
        plt.xlabel("Fecha")
        plt.ylabel("Ventas")
        plt.show()

    logging.info("EDA final completado.")
