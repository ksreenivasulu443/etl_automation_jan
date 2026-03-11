import pandas as pd
import snowflake.connector as snow
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


def read_db(db_creds_file, query=None,env='qa'):
    creds = pd.read_excel(db_creds_file)
    credentials = creds.query(f"env == '{env}' ")

    print(credentials)
    print(credentials.iloc[0,1])
    # conn = snow.connect(
    #     user=credentials.iloc[0,1],
    #     password=credentials.iloc[0,2],
    #     account=credentials.iloc[0,3],
    #     warehouse=credentials.iloc[0,4],
    #
    # )

    conn = snow.connect(
        user=creds.loc[0, 'username'],
        password=creds.loc[0, 'password'],
        account=creds.loc[0, 'account'],
        warehouse=creds.loc[0, 'warehouse']
    )

    df = pd.read_sql(sql=query, con=conn)

    return df


# df = read_db(db_creds_file='/Users/admin/PycharmProjects/etl_automation_jan/test_automation_framework/configs/creds_file.xlsx',
#         env='snowflake_uat',
#              query='Select * from CONTACT.PUBLIC.CONTACT_INFO' )
#
#
# print(df)





