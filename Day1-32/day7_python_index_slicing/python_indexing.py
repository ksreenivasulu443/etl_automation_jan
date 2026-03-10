""" Document strings
This python_indexing.py is created to practice python str methods
created by: Sreeni
created date : 22nd January 2026
updated by:
updated date:
version: v1
"""
# Indexing - accessing a single character from a collection datatype str, list, dict, set, frozenset,numpy array, series, pandas df, polar, duck db
# Slicing - extracting substring of a str, one or more characters #str, list, dict, set, frozenset,numpy array, series, pandas df, polar, duck db

str1 = 'ETL AUTOMATION'

# SYTAX OF INDEXING

#variable[index] ==> index is integer starts 0

print("0 index character",str1[0])
print("1 index character",str1[1])
print("2 index character",str1[2])
print("3 index character",str1[3])
print("4 index character",str1[4])
print("5 index character",str1[5])
print("6 index character",str1[6])
print("7 index character",str1[7])
print("8 index character",str1[8])
print("9 index character",str1[9])
print("10 index character",str1[10])
print("11 index character",str1[11])
print("12 index character",str1[12])
print("13 index character",str1[13])
#print("14 index character",str1[100])# 100 index is not present in the str, we get error index out of range error

str2 = 'SREENI'
print("lengtgh of str2", len(str2))
print("1st character", str2[0])
print("last character", str2[len(str2)-1])

str3 = 'MICROSOFT' # 0 to 8
print("1st character", str3[0])
print("last character", str3[len(str3)-1]) # str3[9-1]

str4 = 'COGNIZANT'

# print("last character", str4[9])

#============================================================================
#NEGATIVE INDEXING
#============================================================================
#============================================================================
str5 = 'HOME'
print("-1 index character",str5[-1])
print("-2 index character",str5[-2])
print("-3 index character",str5[-3])
print("-4 index character",str5[-5])

# FETCH THE FIRST CHARACTER FROM A STRING USING NEGATIVE INDEX DYNAMICALLY
print("first character using -ve index", str5[-len(str5)])


print("1st character", str3[1.0])






