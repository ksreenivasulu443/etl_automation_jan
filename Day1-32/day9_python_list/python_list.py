#
#
# ls_empty = []
#
# ls_empty1 = list()
#
# ls_one_value = [1]
#
# ls_two_values = [1,2]
#
# ls_three_values = [1,2,3.14]
#
# print("ls_empty", ls_empty)
# print("ls_empty1", ls_empty1)
#
# print("ls_empty1", ls_empty, type(ls_empty))
# print("ls_one_value", ls_one_value, type(ls_one_value))
#
# print("ls_two_value", ls_two_values, type(ls_two_values))
#
# print("ls_three_value", ls_three_values, type(ls_three_values))
#
#
# ls = [1, 3.1, True, 'January', 1+2j]
#
# print("ls is", ls, type(ls), id(ls))
# print("methods", dir(ls))
#
# ls2 = [1]
# ls3 = [1]
#
# print("ls2 details", ls2, type(ls2), id(ls2))
# print("ls3 details", ls3, type(ls3), id(ls3))
#
# ls2.append(5)
#
# print("ls2 details after append 5", ls2, type(ls2), id(ls2))
#
# ls2.append(7)
# print("ls2 details after append 7", ls2, type(ls2), id(ls2))
#
#
# ls2.clear()
# print("ls2 details after clear", ls2, type(ls2), id(ls2))
#
# str1 = 'ETL automation'
#
# str2 = 'ETL automation'
#
# # str1 = str1.upper()
#
# print(str1.upper())
#
# print("str1",str1, id(str1), type(str1), dir(str1))
# print("str2",str2, id(str2), type(str2))
# # All fundamental types are immutable in nature meaning you can't change the data (int, float, str, boolean, complex)
#
#



ls = [] # or list()
print("ls is ", ls, type(ls), id(ls), dir(ls), ls.__sizeof__())


###Add elements to list###

ls.append(0)
print("ls after append 0 ", ls, type(ls), id(ls))

ls.append("etl automation")
ls.append(1.4)
ls.append(True)
print("ls after append etl automation ", ls, type(ls), id(ls))

print("ls[0]", ls[0], type(ls[0]))
print("ls[1]", ls[1], ls[1][0:3], type(ls[1]))
print("ls[2]", ls[2], type(ls[2]))
print("ls[3]", ls[3], type(ls[3])) # it can hold heterogeneous elements


ls = [1,6,8,12,3,9,-9, 10, 1]
ls2 = [1,6,8,12,3,9,-9, 10, 1]
a = 1
print("ls3 is", ls, ls2, id(ls), id(ls2))

print(ls[0], type(ls[0]), id(ls[0]))
print(ls2[-1], type(ls2[-1]), id(ls2[-1]))
print(a, type(a), id(a))

ls = [1,6,8,12,3,9,-9, 10, 1]

ls.remove(1)

print("ls after remove", ls)

ls.insert(0,304)

print("ls after insert", ls)
9008760800
ls = []
print(ls,ls.__sizeof__())
ls.append(1)
ls.append('etl')
ls.append(1+2j)
ls.extend([1,2,3,43,2,43,5,34,65,34,76,5,47,6,48,678,76,679,789,678])
print(ls, ls.__sizeof__())

