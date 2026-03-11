import pandas as pd
import numpy as np
from pandasql import sqldf


# df_using_csv = pd.read_csv(r"/Users/admin/PycharmProjects/etl_automation_jan/day30_python_pandas/input_files/sample_csv_source.csv",
#                            names = ['sno','name','loc'],
#                            nrows= 2)
#
# print(df_using_csv)
# print(df_using_csv.columns)
# print(df_using_csv.dtypes)


# df_using_two_header = pd.read_csv(filepath_or_buffer="/Users/admin/PycharmProjects/etl_automation_jan/day30_python_pandas/input_files/two_header.csv",
#                                   header=2,skipfooter=3)
#
# print(df_using_two_header)
# print(df_using_two_header.columns)
# print(df_using_two_header.dtypes)


# df = pd.read_csv(r"/Users/admin/PycharmProjects/etl_automation_jan/day30_python_pandas/input_files/sample_csv_pipe.csv",names=['sno','name','loc'], sep='|')
#
# print(df)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)

# df_excel = pd.read_excel(r"/Users/admin/PycharmProjects/etl_automation_jan/day30_python_pandas/input_files/Master_Test_Template.xlsx")
# print(df_excel)

df_excel_sheet1 = pd.read_excel(r"/Users/admin/PycharmProjects/etl_automation_jan/day30_python_pandas/input_files/Contact_info.xlsx", sheet_name='Sheet2')
print(df_excel_sheet1)


df_par = pd.read_parquet(r"/Day1-32/day30_python_pandas/input_files/userdata1.parquet")
print(df_par)


df_par.to_csv("export_02032025.csv", sep='|')

