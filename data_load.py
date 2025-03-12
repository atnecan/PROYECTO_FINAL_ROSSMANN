# data_load.py

import os
import logging
import pandas as pd

def load_train_store_data(train_path: str, store_path: str):
    """
    Carga los archivos CSV de train y store.
    Maneja errores si los archivos no existen o tienen problemas de lectura.
    
    :param train_path: Ruta al archivo train.csv (por ejemplo: "DATA/train.csv")
    :param store_path: Ruta al archivo store.csv (por ejemplo: "DATA/store.csv")
    :return: (train_df, store_df) -> Dos DataFrames de pandas
    """
    if not os.path.exists(train_path):
        logging.error(f"No se encontró el archivo: {train_path}")
        raise FileNotFoundError(f"No se encontró el archivo: {train_path}")
    if not os.path.exists(store_path):
        logging.error(f"No se encontró el archivo: {store_path}")
        raise FileNotFoundError(f"No se encontró el archivo: {store_path}")

    try:
        train_df = pd.read_csv(train_path, parse_dates=['Date'])
        store_df = pd.read_csv(store_path)
        logging.info("Archivos train y store cargados correctamente.")
        return train_df, store_df
    except Exception as e:
        logging.error(f"Error al leer los archivos CSV: {e}")
        raise

def load_test_data(test_path: str):
    """
    Carga el archivo CSV de test (opcional).
    
    :param test_path: Ruta al archivo test.csv (por ejemplo: "DATA/test.csv")
    :return: test_df -> DataFrame de pandas
    """
    if not os.path.exists(test_path):
        logging.error(f"No se encontró el archivo: {test_path}")
        raise FileNotFoundError(f"No se encontró el archivo: {test_path}")

    try:
        test_df = pd.read_csv(test_path, parse_dates=['Date'])
        logging.info("Archivo test cargado correctamente.")
        return test_df
    except Exception as e:
        logging.error(f"Error al leer el archivo test CSV: {e}")
        raise
