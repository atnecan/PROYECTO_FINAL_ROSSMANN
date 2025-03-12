# data_cleaning.py

import logging
import pandas as pd
import numpy as np

def clean_and_transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica limpieza y transformaciones al DataFrame unificado.
    1. Manejo de valores nulos (CompetitionDistance, CompetitionOpenSince, Promo2).
    2. Creación de variables nuevas (Year, Month, Day, WeekOfYear, etc.).
    3. Filtrado de datos (tiendas cerradas, ventas = 0, outliers).

    :param df: DataFrame resultante de la unión (train + store)
    :return: DataFrame limpio y transformado
    """
    logging.info("Iniciando limpieza y transformación de datos...")

    # 1. Manejo de valores nulos
    if 'CompetitionDistance' in df.columns:
        median_distance = df['CompetitionDistance'].median()
        df['CompetitionDistance'].fillna(median_distance, inplace=True)

    for col in ['CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear']:
        if col in df.columns:
            df[col].fillna(0, inplace=True)

    for col in ['Promo2SinceWeek', 'Promo2SinceYear']:
        if col in df.columns:
            df[col].fillna(0, inplace=True)

    if 'PromoInterval' in df.columns:
        df['PromoInterval'].fillna('None', inplace=True)

    # 2. Creación de columnas de fecha
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df['Day'] = df['Date'].dt.day
        df['WeekOfYear'] = df['Date'].dt.isocalendar().week

    # 3. Filtrado de datos
    if 'Open' in df.columns:
        df = df[df['Open'] == 1].copy()

    if 'Sales' in df.columns:
        df = df[df['Sales'] > 0].copy()
        upper_limit = df['Sales'].quantile(0.99)
        df = df[df['Sales'] < upper_limit].copy()

    logging.info("Limpieza y transformación completadas con éxito.")
    return df
