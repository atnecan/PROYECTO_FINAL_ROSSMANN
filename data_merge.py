# data_merge.py

import logging
import pandas as pd

def merge_data(train_df: pd.DataFrame, store_df: pd.DataFrame) -> pd.DataFrame:
    """
    Une los DataFrames de train y store con la columna 'Store'.
    
    :param train_df: DataFrame con datos de ventas (train)
    :param store_df: DataFrame con datos de las tiendas (store)
    :return: DataFrame unificado (rossmann_df, por ejemplo)
    """
    try:
        df_merged = pd.merge(train_df, store_df, on='Store', how='left')
        logging.info("Unión de DataFrames (train y store) completada correctamente.")
        return df_merged
    except KeyError as e:
        logging.error(f"Error de clave en la unión de DataFrames: {e}")
        raise
    except Exception as e:
        logging.error(f"Error inesperado en la unión de DataFrames: {e}")
        raise
