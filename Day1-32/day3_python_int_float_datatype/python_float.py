''' Document strings
This python_float.py is created to practice python float datatype
created by: Sreeni
created date : 14th January 2026
updated by:
updated date:
version:
'''

a  = 10.000001

print("a value is", a)
print("a datatype is", type(a))
print("a id is", id(a))
print("a size is", a.__sizeof__()) # method/function starts with __(double underscore) its special method in python
print("methods available in int type", dir(a))

b  = -10.5

print("b value is", b)
print("b datatype is", type(b))
print("b id is", id(b))
print("b size is", b.__sizeof__()) # method/function starts with __(double underscore) its special method in python
print("methods available in int type", dir(b))


d = 1e2 #==>1*10^2

print("d value is", d)
print("d datatype is", type(d))


f = 1e12

print("f value is", f)
print("f datatype is", type(f))

#######when we can use float in our ETL testing??
# amount
# salary
# aggressions
# percentage
# Interest rate