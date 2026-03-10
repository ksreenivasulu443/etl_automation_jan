import numpy as np
#
# arr = np.array([1,2,3])
#
# # ls = [1,2,3,4]
# # t =(1,2,3,4)
# # d = {1:1, 2:4, 3:9}
# # s = {1,2,3}
# # fs = frozenset(s)
#
# print("arr details", arr, type(arr), id(arr))
# print("arr methods", dir(arr))




arr = np.array([True,2]) # numpy array holds only homogeneous elements

#str>complex>float>int>bool

print(arr, type(arr))
print("arr[0]",arr[0], type(arr[0]))
print("arr[1]",arr[1], type(arr[1]))
# print("arr[2]",arr[2], type(arr[2]))
# print("arr[3]",arr[3], type(arr[3]))
# print("arr[4]",arr[4], type(arr[4]))

arr = np.array([4.5,2.5,1])
arr1 = np.array([4.5,2.5,1])
print("arr methods", dir(arr))

np.equal([arr, arr1])

print(arr.shape())
print(arr.size())






import time
import numpy as np

# Create large dataset
size = 10000000

# Python List
python_list = list(range(size))

# NumPy Array
numpy_array = np.array(python_list)

# -----------------------------
# Python List Performance
# -----------------------------
start = time.time()
max_list = sum(python_list)
end = time.time()

print("Python List Max:", max_list)
print("Python List Time:", end - start, "seconds")

# -----------------------------
# NumPy Array Performance
# -----------------------------
start = time.time()
max_array = np.sum(numpy_array)
end = time.time()

print("NumPy Array Max:", max_array)
print("NumPy Array Time:", end - start, "seconds")

np.random





