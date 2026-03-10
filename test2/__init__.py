import pandas as pd
import numpy as np

print("pandas", dir(pd))


# df = pd.DataFrame
#Empty dataframe
# df_empty = pd.DataFrame()
#
# print("df4 is", df_empty)
#
d = {'col1': [1, 2], 'col2': [3, 4]}
print("d is", d)
df_dict = pd.DataFrame(data=d)
print(df_dict)
#
# # def f(a,b):
# #     pass
# #
# # f(a=5, b=10)
#
# #pandas DF using numpy array
# df2 = pd.DataFrame(data= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(df2)
#
#
# data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
# print("data is", data)
#
# data2 =  np.random.randint(0,49,(100,7))
# print(data2)
#
# df_array = pd.DataFrame(data = data2)
#
# print("df_array" )
#
# print(df_array)

# dataframe can be created - list, tuple, dict, set, fs, numpy array, series, files, databases, etc

ls = [[1,2,3], [4,5,6],[7,8,9.6],[10,11,12]]

# ls =[1,2,3]

df_list = pd.DataFrame(data=ls, columns= ['id','age','sal'])

print("df_list" )

print(df_list)

print("shape",df_list.shape)
print("columns", df_list.columns)
print("dtypes", df_list.dtypes)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
df_csv = pd.read_csv("/old/Day29_pandas/COVID clinical trials.csv")

print(df_csv)










