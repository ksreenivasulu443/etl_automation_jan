# Slicing means extracting a part (substring) of a string by giving a range of positions.
# slicing is not just for string, we can also slice list, tuple, dict, set, frozenset, range

#  variable/string[start:stop:step] # start, stop and step are integer
#  **start**: The index of the first character to include in the slice (default is 0).
#  **stop**: The index where slicing stops (exclusive). till last
#  **step**: The interval between characters in the slice (default is 1).

str1 = 'ETL AUTOMATION'
print("str1[:]",str1[:] ) # str1[0:len(str1)-1,1]
print("str1[4:]",str1[4:] ) #str1[4:len(str1)-1]

print("str1[:3]",str1[:3], len(str1[:3]) ) #str1[0:3]

print("string[2:10:1]",str1[2:10:1])
print("string[2:100:1]",str1[2:100:1])

print("string[200:1000:1]",str1[-200:1000:400])

print("string[::2]",str1[::3])

#gmail --> provide, domain, username

katsreen100@gmail.com
katsreen100@yahoo.com
