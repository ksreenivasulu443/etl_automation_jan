import pandas as pd
import numpy as np
from pandasql import sqldf

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
#
# # # dictionary data which few records information
# data = {
#     "cust_id": [101, 102, 103, 104, 105],
#     "full_name": ["Ram", "Ravi", "Alok", "DANA", None],
#     "product": ["Laptop", "Phone", np.nan, "Tablet", "Monitor"],
#     "quantity": [1, 2, 1, None, 2],
#     "purchasedate": pd.to_datetime(["2024-05-01", None, "2024-05-05", "2024-05-06", "2024-05-07"])
# }
#
# df = pd.DataFrame(data=data)
#
# ###selection of columns and rows
#
# print("All rows and columns")
# print(df)
#
#
#
# print("Top n rows")
# print(df.head(n=3))
#
# print(df.head()) # top 5 rows because n default is 5
#
# print("bottom n rows")
#
# print(df.tail(n=2))
#
# print(df.tail()) # default n = 5

#Select sample rows from dataframe

df = pd.read_csv(r"/Users/admin/PycharmProjects/etl_automation_jan/Day1-32/day31_python_pandas_part2/input_files/IPL Matches 2008-2020.csv")


# print(df)
#
# print("random n records")
# print(df.sample(n=2))
#
# print(df.sample(frac=0.01))


# statistics & generic methods

# print("statitics")
print(df.describe())
#
# print(df.dtypes)
#
print(df.columns)
#
print(df.info())

# selecting rows and columns

# select col1 from table

# print(df.umpire1) # selecting one column from dataframe, column has spaces . syntax not works
# print(df['umpire1']) # selecting one column from dataframe when columns has spaces
#
# print(df[['umpire1','umpire2']]) # selecting one/more columns from dataframe
# print(df.columns)
# print(df['winner'].nunique())
# print("=="*100)
# print(df['salary'].nsmallest(10))
#
# print(df['result_margin'].nlargest(5))

# print(sqldf("select umpire1, umpire2 from df"))

# selecting rows and columns from indexes

# print(df)
# # o index row and all the columns
# # print(df.iloc[-1:-5:-1])
#
# print(df.iloc[0:5,4: ])  # index locations


# # selecting rows and columns from labels

# print(df.loc[0:4,'id':'venue'])
#
# print(df.loc[0:4,['id','city','venue']])
#
#
# print(df.loc[[45,9,2,6,1],['id','city','venue']])


data = {
    "cust_id": [101, 102, 103, 104, 105],
    "full_name": ["Ram", "Ravi", "Alok", "DANA", None],
    "product": ["Laptop", "Phone", np.nan, "Tablet", "Monitor"],
    "quantity": [1, 2, 1, None, 2],
    "purchasedate": pd.to_datetime(["2024-05-01", None, "2024-05-05", "2024-05-06", "2024-05-07"])
}

df = pd.DataFrame(data=data)

print(df)

print(df.iat[4,2])

print(df.at[3,'full_name'])

df = pd.read_excel('/Users/admin/PycharmProjects/august_2025_automation/old/test_automation_framework/creds_file.xlsx')

print(df)

print(df.at[0,'password'])

print(df.iat[0,2])

df = df.set_index("database_type")

print(df)

print(df.at['snowflake_qa','password'])

print(df.at['snowflake_uat','password'])

len(df)

df.shape



