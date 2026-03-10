import pandas as pd

from pandasql import sqldf

sales = pd.DataFrame({
    "dept":["IT","IT","HR","HR","Finance"],
    "salary":[100,200,150,300,250],
    "region":['A',"B","A","A","A"]
})

# print(sqldf("""select count(1), sum(salary),
#                 min(salary), max(salary), avg(salary) from sales
#             """))
# print("="*100)
# print(sales['salary'].sum())
# print(sales['salary'].count())
# print(sales['salary'].max())
# print(sales['salary'].min())
# print(sales['salary'].mean())
#
# print("="*100)
#
# print(sales.agg({'salary':['count','min','max','sum','mean']}))
#
# print(sales['salary'].agg(['count','min','max','sum','mean']))
#
# print("="*100)
#
# print(sqldf("select dept,region, count(1),sum(salary), min(salary), max(salary), avg(salary) from sales group by dept,region"))
#
# print("="*100)
# print(sales.groupby("dept")['salary'].count())
#
# print(sales.shape)
#
# print(sales.groupby("dept")['salary'].sum())
# print("="*100)
# print(sales.groupby("dept")["salary"].agg(["sum","mean","max","count","mean"]))
#
# print(sales.groupby(["dept","region"])["salary"].agg(["count"]).reset_index())
# print("="*100)
# print(sqldf("select dept, count(1) from sales group by dept having count(1)>1"))
# print("="*100)
# print(sales)
# print("="*100)
# print(sales.duplicated(subset=['dept']).sum())
#
# duplicates = sales.groupby("dept").size().reset_index(name="count")

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df = pd.read_csv("/Users/admin/PycharmProjects/etl_automation_jan/Day1-32/day30_python_pandas/input_files/Contact_info_7.csv")

print(df)

print(sqldf("select identifier, count(1) from df group by identifier having count(1)>1"))

print("="*100)
# print(df.duplicated().sum())


df_count = df.groupby("Identifier")['Surname'].count().reset_index(name="count")
#
# print(df_count)
#
# print(type(df_count))
#
# print(df.apply(lambda x: x.duplicated().sum()))

duplicates = df.groupby("Identifier").size().reset_index(name="count")

print(duplicates.query('count > 1'))

print("="*100)

df_count = df.groupby("Identifier")['Surname'].count().reset_index(name="count")

print(df_count.query('count > 1'))

### problems with pandas

sqldf("select *, dense_rank() over (order by salary) as dnr from df")









