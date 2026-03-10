# import pandas as pd
#
# employees = pd.DataFrame({
#     "emp_id":[1,2,3,4],
#     "name":["John","Mike","Sara","Anna"],
#     "dept_id":[101,101,103,104]
# })
#
# departments = pd.DataFrame({
#     "dept_id":[101,102,103],
#     "dept_name":["HR","IT","Finance"]
# })
#
#
# df_j= pd.merge(employees, departments, on="dept_id", how="inner")
#
# print(df_j)
#
#
# sales = pd.DataFrame({
#     "dept":["IT","IT","HR","HR","Finance"],
#     "sales":[100,200,150,300,250],
#     "region":['A',"B","A","A","A"]
# })
#
# df_g = sales.groupby("dept")["sales"].sum()
#
# print(df_g)
#
#
# df_g = sales.groupby("dept")["sales"].agg(["sum","mean","max"])
#
# print(df_g)
#
# print(sales.groupby(["dept","region"])["sales"].count())