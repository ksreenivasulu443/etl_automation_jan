import pandas as pd
import numpy as np
from pandasql import sqldf

df = pd.DataFrame()

print("df is", df)
print("df type", type(df))
print("df shape ", df.shape)

print("="*100)
d = {'col1': [1, 2, 4], 'col2': [3, 4,None]}
print("d is", d)
df_using_dict = pd.DataFrame(data=d)

print("df_using_dict is")
print(df_using_dict)
print("df_using_dict type", type(df_using_dict))
print("df_using_dict shape ", df_using_dict.shape)
print("df_using_dict.columns", df_using_dict.columns)

#============================================================================================================
print("="*100)
l = [[1,2,3],[4,5,6],[7,8,9]]
print("l is", l, type(l))
df_using_list = pd.DataFrame(data=l, columns=['sno','age','sal'])

print("df_using_list is")
print(df_using_list)
print("df_using_list type", type(df_using_list))
print("df_using_list shape ", df_using_list.shape)

print("df.columns", df_using_list.columns)


#============================================================================================================
print("="*100)
l = ((1,2,3),(4,5,6),(7,8,9))
print("l is", l, type(l))
df_using_tuple = pd.DataFrame(data=l, columns=['sno','age','sal'])

print("df_using_tuple is")
print(df_using_tuple)
print("df_using_tuple type", type(df_using_tuple))
print("df_using_tuple shape ", df_using_tuple.shape)

print("df_using_tuple.columns", df_using_tuple.columns)

#============================================================================================================
print("="*100)
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("arr is", arr, type(arr))
df_using_arr = pd.DataFrame(data=arr, columns=['sno','age','sal'])

print("df_using_arr is")
print(df_using_arr)
print("df_using_arr type", type(df_using_arr))
print("df_using_arr shape ", df_using_arr.shape)

print("df_using_arr.columns", df_using_arr.columns)

# Dataframe 10 rows & 5 columns random data

arr_random = np.random.randint(1,100,(100,5))

df_using_arr_random = pd.DataFrame(data=arr_random, columns=['sno','age','sal','dept_id','pincode'])

print("df_using_arr_random is")
print(df_using_arr_random)
print("df_using_arr_random type", type(df_using_arr_random))
print("df_using_arr_random shape ", df_using_arr_random.shape)

print("df_using_arr_random.columns", df_using_arr_random.columns)

###########################################################################

df_using_csv = pd.read_csv(r"/Day1-32/day30_python_pandas/input_files/sample_csv_source.csv")

print(df_using_csv)
print(df_using_csv.columns)
print(df_using_csv.dtypes)

print(sqldf("select sno, lower(name) as lower_name, loc from df_using_csv where loc='HYD' "))

print(sqldf("""select sno, count(1) from df_using_csv 
group by sno having count(1)>1"""))
