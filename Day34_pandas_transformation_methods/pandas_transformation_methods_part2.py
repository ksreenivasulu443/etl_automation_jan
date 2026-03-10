import pandas as pd
import numpy as np
from pandasql import sqldf
#
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)
#
# emp = pd.DataFrame({
#     "emp_id":[1,2,3,4],
#     "name":["John","Mike","Sara","Anna"],
#     "dept_id":[101,101,103,104]
# })
#
# dept = pd.DataFrame({
#     "dept_id":[101,102,103],
#     "dept_name":["HR","IT","Finance"]
# })
#
#
# print("emp df")
# print(emp)
# print("="*100)
#
# print("dept df")
# print(dept)
# print("="*100)
# print("Inner join")
# print(pd.merge(left=emp, right=dept, on='dept_id', how='inner'))
# print("="*100)
# print(sqldf("""select * from emp inner join dept
#                 on emp.dept_id= dept.dept_id"""))
#
# print("="*100)
# print("left join")
# print(pd.merge(left=emp, right=dept, on='dept_id', how='left'))
# print("="*100)
# print(sqldf("""select emp.emp_id, emp.name, emp.dept_id, dept.dept_name from emp left join dept
#                 on emp.dept_id= dept.dept_id"""))
#
# print("="*100)
# print("right join")
# print(pd.merge(left=emp, right=dept, on='dept_id', how='right'))
# print("="*100)
# print(sqldf("""select * from emp right join dept
#                 on emp.dept_id= dept.dept_id"""))
#
# print("="*100)
# print("full join")
# print(pd.merge(left=emp, right=dept, on='dept_id', how='outer'))
# print("="*100)
# print(sqldf("""select * from emp full join dept
#                 on emp.dept_id= dept.dept_id"""))
#
# df_full = pd.merge(emp, dept, on='dept_id', how='outer')
#
# print(df_full)
#
# # print("sort")
#
# # print(df_full.sort_values('dept_id', ascending=False, inplace=True))
#
# # df_full = df_full.rename(columns = {'dept_name':'dept_location','emp_id':'emp_no'})
#
# # df_full.rename(columns = {'dept_name':'dept_location','emp_id':'emp_no'}, inplace=True)
#
# # print(df_full.rename(columns = {'dept_name':'dept_location','emp_id':'emp_no'}))
#
# print(df_full)
#
#
# print(df_full.dropna())
#
# print(df_full.dropna(subset=['dept_name']))
#
# sqldf("select * from df_full where dept_name is not null")

# df_merge = df_emp.merge(df_dept, on='dept_id', how='inner')
# can we use like this also?



emp = pd.DataFrame({
    "emp_id":[1,2,3,4],
    "name":["John","Mike","Sara","Anna"],
    "dept_id":[101,101,103,104]
})

dept = pd.DataFrame({
    "dept_no":[101,102,103],
    "dept_name":["HR","IT","Finance"]
})


df_u = pd.merge(emp, dept,left_on='dept_id', right_on='dept_no')
print("df_u after join")
print(df_u)

df_u['dept_no'] = df_u["dept_no"].astype("float")
print("df_u after type cast")
print(df_u)

# df = pd.merge(
#     orders,
#     sales,
#     on=["order_id","product_id"],
#     how="inner"
# )
#
# df3 = pd.merge(
#     df1,
#     df2,
#     left_on=["order_id","product_code"],
#     right_on=["order_number","product_id"]
# )
#
# df1 =
# df2 =
# df3 =
#
# df4 = pd.merge(df1, df2)
#
# pd.merge(df4,df3, how)


df_full = pd.merge(emp, dept,left_on='dept_id', right_on='dept_no', how='outer')
print("df_full after join")
print(df_full)

print(df_full.fillna(0))

print(df_full.fillna('74235423').fillna({'emp_id':9999.9, 'name':'SREENI', 'dept_name':'NO DEPT'}))

print(df_full.isnull().sum())

import pandas as pd

df = pd.DataFrame({
    "date": ["2024-01-01","2024-01-02","2024-01-03","2024-01-04","2024-01-05"],
    "product": ["Laptop", None, None, "Mobile", None],
    "sales": [100,120,150,200,180]
})

print(df)

print(df.fillna(method="ffill"))

# SELECT
#     date,
#     LAST_VALUE(product IGNORE NULLS)
#     OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS product,
#     sales
# FROM sales_data;

# parquet, delta tables, lake house --> parquet


import pandas as pd

df1 = pd.DataFrame({
    "product":["Laptop","Mobile","B"],
    "salary":[1000,800,900]
})


df2= pd.DataFrame({
    "product":["ipad","Mobile"],
    "sales":[100,800],
    "prodcy_cat":['A',"B"]
})

print(pd.concat([df1,df2], axis=1))

df1 = pd.DataFrame({
    "product":["Laptop","Mobile","B"],
    "salary":[1000,800,900]
})

df2 = pd.DataFrame({
    "product":["Lapt","Mobile","B"]
})

print(df1.compare(df2))







