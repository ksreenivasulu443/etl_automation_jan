import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
def read_file(file_path, file_type, user_sep, user_header,env='qa'):
    file_type = file_type.lower()
    if file_type == 'csv':
        df = pd.read_csv(file_path,sep=user_sep, header=user_header)
    elif file_type == 'excel':
        df = pd.read_excel(file_path, header=user_header)
    elif file_type == 'txt':
        df = pd.read_csv(file_path,sep=user_sep, header=user_header)
    elif file_type == 'parquet':
        df = pd.read_parquet(file_path)
    elif file_type == 'json':
        df = pd.read_json(file_path)
    elif file_type == 'xml':
        df = pd.read_xml(file_path)
    else:

        print("user entered format is not supported. Plz try csv,txt, excel, parquet,json,xml")

    return df





