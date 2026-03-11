from pandasql import sqldf
def count_validation(source, target):
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




def duplicate_validation(df,primary_keys):
    print("="*100)
    print("Duplicate validation has started")
    print("="*100)
    duplicates = df.groupby(primary_keys).size().reset_index(name='count').query('count>1')
    #duplicates = sqldf(f"select {pkey}, count(1) from target_df group by {pkey} having count(1)>1 ")

    print("duplicates dataframe")
    if len(duplicates)>0:
        print("Duplicates present.Below is sample primary_keys")
        print(duplicates)
    else:
        print("No duplicates present!")
    print("="*100)
    print("Duplicate validation has completed")
    print("="*100)


def unique_validation(df,unique_columns):
    print("="*100)
    print("unique validation has started")
    print("="*100)
    for col in unique_columns:
        unique_df = df.groupby(col).size().reset_index(name='count').query('count>1')
        print("duplicates dataframe")
        if len(unique_df)>0:
            print("Duplicates present.Below is sample pkeys")
            print(unique_df)
        else:
            print("No duplicates present!")

    print("="*100)
    print("Duplicate validation has completed")
    print("="*100)


def null_check(df,not_null_columns):
    print("=" * 100)
    print("Null validation has started")
    # null_column_list = str(not_null_columns).split(',')
    for col in not_null_columns:
        null_rows = df[df[col].isnull()]
        print("null rows", null_rows)
        #null_rows = sqldf(f"select * from df where {col} is null")
        if null_rows.shape[0]>0:
            print(f" {col} Null rows present")
        else:
            print(f" {col} No nulls presennt")
    print("=" * 100)
    print("Null validation has been complete")


def data_compare(source,target):
    print("="*100)
    print("Data compare validation has started")
    query = """select a.*,'source' from (select * from source except select * from target) a 
                union all
                select b.*,'target' from (select * from target except select * from source) b"""
    failed = sqldf(query)
    if len(failed)>0:
        print("data is not matching")
        print(failed)
    else:
        print("data is matching")

    print("="*100)
    print("Data compare validation has completed")
    print("="*100)

def schema_check(source, target):
    source_columns = set(source.columns)
    target_columns = set(target.columns)
    diff = source_columns.difference(target_columns)
    if len(diff)>0:
        print("schema is not matching")
        print(diff)
    else:
        print("schema is matching")



