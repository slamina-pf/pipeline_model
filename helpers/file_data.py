import pyarrow.parquet as pq
from helpers.constants import TEMP_DATA_GENERAL_PATH
import pandas as pd
from joblib import dump, load

def read_parquet_file(file_path: str):
    table = pq.read_table(f'{TEMP_DATA_GENERAL_PATH}/{file_path}')
    return table.to_pandas()

def save_parquet_file(df, file_path: str):
    df = pd.DataFrame(df)
    df.to_parquet(f'{TEMP_DATA_GENERAL_PATH}/{file_path}', index=False)
    return True

def save_model(model, model_name):
    dump(model, f"{TEMP_DATA_GENERAL_PATH}/{model_name}.joblib")

def load_model(model_name):
    return load(f"{TEMP_DATA_GENERAL_PATH}/{model_name}.joblib")