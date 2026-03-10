
import numpy as np
# arr = np.array([4.5,2.5,1])
# arr1 = np.array([4.5,2.5,1.2])
# print("arr methods", dir(arr))
#
# print(np.equal(arr, arr1))
#
# print(arr.shape)
# print(arr.size)
# print('='*100)
# arr_2d = np.array([[1,2,3],[4,5,6]])
# print(arr_2d)
# print("arr_2d.shape", arr_2d.shape)
# print(arr_2d.size)

###random

# print("np.random.rand() output is", np.random.rand()) # single number 0 to 1
#
# print("np.random.rand(5) output is", np.random.rand(4)) # 4 numbers between 0 to 1
#
# print("np.random.rand(5) output is", np.random.rand(4)*100) # # 4 numbers between 0 to 10
#
# # print("np.random.rand(5) output is", np.random.rand(500)*10)
#
# print("np.random.rand(5,5) output is")
# print(np.random.rand(100,5)*10)
#
# print("np.random.randint(0,7)", np.random.randint(0,7)) # 1 random number between 0 to 5
#
# print("np.random.randint(5,10)", np.random.randint(18,101,100))
#
# print("np.random.randint(5,10)", np.random.randint(18,101,(100,1)))


dept = np.array([10, 20, 30, 40, 50])


print(np.random.choice(dept))

tier = np.array(['silver','gold','platinum'])

print(np.random.choice(tier,10, replace=True))