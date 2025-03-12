# main.py

import logging
import pandas as pd
from data_load import load_train_store_data, load_test_data
from data_merge import merge_data
from data_cleaning import clean_and_transform_data
from eda import initial_eda, final_eda

def main():
    """
    Orquesta la ejecución de todo el flujo de trabajo:
    1. Carga de datos (train, store, opcional test)
    2. EDA inicial
    3. Unión (train + store)
    4. Limpieza y transformación
    5. EDA final
    6. Guardado del dataset final
    """

    # Configurar logging
    logging.basicConfig(
        filename="data_cleaning.log",
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.info("Iniciando el proceso principal de limpieza y análisis.")

    # 1. Rutas de archivos
    train_path = "DATA/train.csv"
    store_path = "DATA/store.csv"
    test_path = "DATA/test.csv"  # opcional

    # 2. Carga de datos
    train_df, store_df = load_train_store_data(train_path, store_path)

    # (Opcional) cargar test
    try:
        test_df = load_test_data(test_path)
        logging.info(f"Archivo test.csv cargado: {test_df.shape}")
    except FileNotFoundError:
        test_df = None
        logging.warning("No se encontró test.csv, se continuará sin datos de test.")

    # 3. EDA inicial (antes de limpiar)
    initial_eda(train_df)

    # 4. Unión de dataframes (train y store)
    rossmann_df = merge_data(train_df, store_df)

    # 5. Limpieza y transformación
    rossmann_cleaned = clean_and_transform_data(rossmann_df)

    # 6. EDA final (después de limpiar)
    final_eda(rossmann_cleaned)

    # 7. Guardar resultado final
    output_path = "DATA/rossmann_final.csv"
    rossmann_cleaned.to_csv(output_path, index=False)
    logging.info(f"Datos limpios guardados en: {output_path}")
    print(f"Datos limpios guardados en: {output_path}")

    logging.info("Proceso completado con éxito.")

if __name__ == "__main__":
    main()
