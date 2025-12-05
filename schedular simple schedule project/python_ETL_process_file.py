# PYTHON ETL PROCESS TO CONNECT THE PYTHON AIRFLOW FILE USING WRAPPER SHELL .
# There are 3 files merge to show the files to web UI.
import mysql
import pymysql
import pandas as pd
from datetime import datetime
import os

from jdbc_connectivity import connection


def fetch_data_code_from_mysql():
    mysql_config = {
        "host" : "localhost",
        "user":"root",
        "password":"root",
        "data_base":"etl_example"
    }
    connection = pymysql.connect(**mysql_config)
    query = "SELECT * FROM sample_data"
    df = pd.read_sql(query,connection)
    return df

def transform_data(df):
    df_transformed = df[df ["age"]>30]
    return df_transformed

def write_data_to_file(df):
    output_dir = "/home/jerry0104/extract"
    os.makedirs(output_dir,exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%D%H%M%S")
    file_name = f"etl_output_{timestamp}.csv"
    file_path=os.path.join(output_dir,file_name)
    df.to_csv(file_path,index=False)
    print(f"Data written to {file_path}")

def etl_process():
    df = fetch_data_code_from_mysql()
    df_transformed = transform_data(df)
    write_data_to_file(df_transformed)

if __name__ == "__main__":
    etl_process()

# check the package:
# pip install pandas
# pip install mysql-connector
# pip install --upgrade mysql-connector-python
# pip install pymysql