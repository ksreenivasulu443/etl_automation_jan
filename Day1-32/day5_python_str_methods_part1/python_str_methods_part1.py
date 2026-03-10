""" Document strings
This python_str_methods_part1.py is created to practice python str methods
created by: Sreeni
created date : 20th January 2026
updated by:
updated date:
version: v1
"""
import sys
str1 = "etl automaTion Labs"

print("Value of str1", str1, type(str1), id(str1), sys.getsizeof(str1) )

print(" str methods available", dir(str1))

print(" int methods available", dir(1))

print(" float methods available", dir(1.1))

# syntax to use datatype methods
# variable/value.methodname(parameters)
str1 = "etl automaTion Labs"
print("str1.lower() o/p", str1.lower()) # str1.lower() takes only one argument i.e self, Value of self will be taken care by PVM

# len, type, id, dir  ==> built in functions ==> build_func_name(variable/method)

print("str1.upper() o/p", str1.upper())

# TYPE CASTING

print("sreeniVsuluKattubadi".lower())

import builtins
print(dir(builtins))


print("str1.lower() o/p   ", str1.lower())
print("str1.casefold() o/p", str1.casefold())

str2 = "straße"
print("str2.lower() o/p   ", str2.lower())
print("str2.casefold() o/p", str2.casefold())

str3 = "İSTANBUL"
print("str3.lower() o/p   ", str3.lower())
print("str3.casefold() o/p", str3.casefold())

str4 = 'Etl auTomation laBs'

print( str4.capitalize())
print( str4.title())

print("cap   ", str4.capitalize())
print("tit", str4.title()) # Sreenivas Kattubadi

print("swap   ", str4.swapcase())

str5 = ' EtL Automation Labs         '

print("len of str5", len(str5))

print("strip", str5.strip(), len(str5.strip()))
print("lstrip", str5.lstrip(), len(str5.lstrip()))
print("rstrip", str5.rstrip(), len(str5.rstrip()))

str6 = '1423432.Sreenivasulu'

print("strip on str6", str6.strip('1234567890.'), len(str6.strip('11234567890.')))

str7 = 'etlbigdata@gmail.com'

print("startwith", str7.startswith('Etl'))
print("endswith", str7.endswith('com'))

print("endswith", str7.endswith('com'))


