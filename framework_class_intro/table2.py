# file - source (csv)
# snowflake - target

import snowflake.connector as snow
import pandas as pd
from pandasql import sqldf

pd.set_option('display.max_columns',None)
pd.set_option('display.width',2000)

source = pd.read_csv('/Users/admin/PycharmProjects/etl_automation_jan/Day1-32/day31_python_pandas_part2/input_files/Contact_info.csv')
# source_v2 = pd.read_csv("/Users/admin/PycharmProjects/etl_automation_jan/Day1-32/day31_python_pandas_part2/input_files/Contact_info_7.csv")
#
# source = pd.concat([source_v1,source_v2])

conn=snow.connect(
    user='KATSREEN100',
    password='Dharmavaram@2026',
    account='bkbnrdx-yg92711',
    warehouse='COMPUTE_WH',
)
target=pd.read_sql(sql=f'select *from CONTACT.PUBLIC.CONTACT_INFO a',con=conn)
print(target)
pkey ='abc'
unique_cols =['IDENTIFIER','SURNAME','GIVEN_NAME']

# Medallian
#
# raw(s3/adls/gs/windows/unix) --> bronze --> silver --> gold


# print("Source count is", len(source), source.shape[0],source.Identifier.count())
# print("target count is", len(target), target.shape[0],target.IDENTIFIER.count())
# count validation

print("="*100)
print("Count validations has started")
print("="*100)
if len(source) == len(target):
    print(f"source count and target count is matching! source count is {len(source)} and target count is {len(target)}")
else:
    print(f"source count and target count is not matching! source count is {len(source)} and target count is {len(target)}")
print("="*100)
print("Count validation has completed")
print("="*100)





print("="*100)
print("Duplicate validation has started")
print("="*100)
duplicates = target.groupby(pkey).size().reset_index(name='count').query('count>1')
print("duplicates dataframe")
if len(duplicates)>0:
    print("Duplicates present.Below is sample pkeys")
    print(duplicates)
else:
    print("No duplicates present!")

print("="*100)
print("Duplicate validation has completed")
print("="*100)



print("="*100)
print("unique validation has started")
print("="*100)

for col in unique_cols:
    unique_df = target.groupby(col).size().reset_index(name='count').query('count>1')
    print("duplicates dataframe")
    if len(unique_df)>0:
        print("Duplicates present.Below is sample pkeys")
        print(unique_df)
    else:
        print("No duplicates present!")

print("="*100)
print("Duplicate validation has completed")
print("="*100)






print("="*100)
print("Data compare validation has started")
#option
print(source.shape)
source.columns = source.columns.str.replace(" ", "_").str.upper()
print(source.columns)
print(target.columns)
#option-1
# print(source == target)
#option-2
print("="*100)
print(source.compare(target)) # rows count, col count and col name should be same


print("="*100)
print("Data compare validation has completed")
print("="*100)

