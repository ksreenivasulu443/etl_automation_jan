# Slicing means extracting a part (substring) of a string by giving a range of positions.
# slicing is not just for string, we can also slice list, tuple, dict, set, frozenset, range

#  variable/string[start:stop:step] # start, stop and step are integer
#  **start**: The index of the first character to include in the slice (default is 0).
#  **stop**: The index where slicing stops (exclusive). till last
#  **step**: The interval between characters in the slice (default is 1).
# 1
# str1 = 'ETL AUTOMATION'
# print("str1[2:2:1]", str1[2:2:1])
#
# print("str1[10:4:1]", str1[10:4:1])
#
# print("str1[2:2:-1]", str1[2:2:-1])
#
# print("str1[-1:-10]", str1[-1:-10])
#
# print("str1[-2:-10:-1]", str1[-2:-10:-1])
#
# dob = '16-05-2000' #dd-mm-yyyy
#
# print("day",dob[0:2])
# print("month",dob[3:5])
# print("year",dob[-4::1])
#
# email = 'katsr@gmail.com'
# print("email last 3 char",email[-10:])
#
#
# print(str1[0:15:2])
#
# print(str1[0:15:3])
#
# # print(str1[0:15:0])
#
# print("str1[5:-5:1]",str1[5:-5:1])
#
# print("str1[0:len(str1):-1]",str1[0:len(str1):-1])
#
# print("str1[::-1]",str1[-1:-len(str):-1])# str1[-1:last:-1]
#
# int
# float
# str(12)

a = 1212
a= str(a)
print(a == a[::-1])