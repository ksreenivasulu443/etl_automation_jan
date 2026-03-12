import pandas as pd

from test_automation_framework.utility.validation_library import null_check
from utility.read_file import read_file
from utility.read_db import read_db
from utility.validation_library import count_validation, duplicate_validation,data_compare,unique_validation


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
total_test_cases = pd.read_excel("/Users/admin/PycharmProjects/etl_automation_jan/test_automation_framework/configs/test_cases.xlsx")
print(total_test_cases)
test_cases = total_test_cases.query("execution_ind=='Y' ")
print(test_cases)





for index, row in test_cases.iterrows():
    print("index is", index)
    print("="*100)
    print("row is")
    print(row)
    print("=" * 100)
    print(type(row))

    print("source type is", row['source_type'])
    print("source path is", row['source_path'])

    print("=" * 100)

    print("target type is", row['target_type'])
    print("target path is", row['target_path'])


    if row['source_type'] == 'database':
        source = read_db(db_creds_file="/Users/admin/PycharmProjects/etl_automation_jan/test_automation_framework/configs/creds_file.xlsx",
                         query=row['source_query'],
                         datata_type=row['database_type'])
    else:
        source = read_file(file_path=row['source_path'],
                           file_type=row['source_type'],
                           user_sep=row['file_separator'] ,
                           user_header=row['file_header'])

    if row['target_type'] == 'database':
        target = read_db(db_creds_file="/Users/admin/PycharmProjects/etl_automation_jan/test_automation_framework/configs/creds_file.xlsx",
                         query=row['target_query'],
                         datata_type=row['database_type'])
    else:
        target = read_file(file_path=row['target_path'],
                           file_type=row['target_type'],
                           user_sep=row['file_separator'],
                           user_header=row['file_header'])

    for val in row['validations'].split(','):
        if val == 'count':
            count_validation(source, target)


        elif val == 'duplicate':
            duplicate_validation(df=target, primary_keys=row['primary_key'])
        elif val == 'null':
            null_check(df=target, not_null_columns=row['not_null_columns'])
        elif val == 'unique':
            unique_validation(df=target,unique_columns=row['unique_columns'])
        elif val == 'data_compare':
            data_compare(source=source, target=target)


