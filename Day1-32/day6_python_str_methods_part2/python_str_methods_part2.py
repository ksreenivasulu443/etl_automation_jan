""" Document strings
This python_str_methods_part2.py is created to practice python str methods
created by: Sreeni
created date : 21st January 2026
updated by:
updated date:
version: v1
"""


# str1 = 'etl automation labs'
#
# print("str1.isalpha()", str1.isalpha())
#
# str2 = 'etl'
#
# print("str2.isalpha()", str2.isalpha()) # surname, firstname, lastname, cityname, statename

#
# str3 = 'etl automation and big data automation '
#
# print("str3.isalnum()", str3.isalnum())
#
# str4 = '5342532'
#
# print("str4.isalnum()", str4.isalnum()) # Address
#
# # name --> upper(name)
#
# name = 'ETL AUTOMATION LABs'
#
# print("name.isupper()", name.isupper())
# print("name.isupper()", name.isalpha())

#test, dev, UAT

# select  id, upper(name) from st
# minus
# select id, name from tt
#
# day1 - pipeline --> upper working file - Aut --looks fine
# day2 - pipeline --> upper working file - Aut --looks fine
# day3 - pipeline -- . name col has introcued some lower -- 2 rows -->
# day4 - pipeline -- . name col has introcued some lower -- 0 rows -->

str1= 'ETL Automation labs'
print("str1 details", str1, type(str1))

print("str1.split()", str1.split(), type(str1.split())) # split always returns list type o/p

pkey_columns = 'id,name,start_date'

print("pkey_columns.split()", pkey_columns.split())
print("pkey_columns.split()", pkey_columns.split(','))

path = '/Day1-32/day6_python_str_methods_part2/python_str_methods_part2.py'
print("path.split()", path.split('/')[-1])

pkey_columns = 'id,name,start_date, end_date'

print("pkey_columns.split()", pkey_columns.split(',',1))

path = '/Day1-32/day6_python_str_methods_part2/python_str_methods_part2.py'
print("path.split()", path.split('/', 5))

path = '/Day1-32/day6_python_str_methods_part2/python_str_methods_part2.py'
print("path.split()", path.rsplit('/', 1))

str1= 'ETL Automation labs'
print("str1 raplace", str1.replace('a','zuyretuywqteryqwt'))

print("str1 raplace", str1.replace('labs','Z'))

phone = '+91-9739896812'

country_code ='+91'

print("phone raplace", phone.replace(' ',''))

str1 = 'ETL Automation labs'

print(str1[-1])

print(str1[4])

print(str1[-15])