import pandas as pd
from utility.read_file import read_file
from utility.validation_library import count_validation, duplicate_validation,data_compare


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
total_test_cases = pd.read_excel("/Users/admin/PycharmProjects/etl_automation_jan/test_automation_framework/configs/test_cases.xlsx")
print(total_test_cases)
test_cases = total_test_cases.query("execution_ind=='Y' ")
print(test_cases)


# ls =[1,2,3,4]
# dict1 = {1:'sreeni', 2:'Ramesh'}
#
# dict1[1]
# for i in ls:
#     print(i)
#
# for key, value in dict1.items():
#     print(key, value)


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

    source = read_file(file_path=row['source_path'],
                       file_type=row['source_type'],
                       user_sep=row['file_separator'] ,
                       user_header=row['file_header'])

    target = read_file(file_path=row['target_path'],
                       file_type=row['target_type'],
                       user_sep="," ,
                       user_header=0)

    print("+"*100)
    print(source)
    print("+" * 100)
    print(target)

    count_validation(source=source,target=target)
    duplicate_validation(df=target,primary_keys=row['primary_key'])
    data_compare(source=source, target=target)

