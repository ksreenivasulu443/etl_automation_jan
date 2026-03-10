#
import sys
ls = []


print("values of ls", ls)
print("type of ls", type(ls))
print("id of ls", id(ls))
print("size of ls", ls.__sizeof__()) # this will not contain GC memmory
print("size of ls", sys.getsizeof(ls)) # this method includes garbage collectors memory
print("methods of ls", dir(ls))
#
# ls.append(1) # Always take element of any type and inserts in the end
#
# print("values of ls after append 1", ls, id(ls))
#
# ls.append(3.2)
#
# print("values of ls after append 3.2", ls, id(ls))
#
# ls.append('etl')
#
# print("values of ls after append etl", ls, id(ls))
#
# ls.append('etl')
#
# print("values of ls after append etl second", ls, id(ls))
#
# ls.append(-999)
#
# print("values of ls after append -999", ls, id(ls))
#
# ls.append(True)
# ls.append(1+2j)
#
# print("values of ls after append bool & complex", ls, id(ls))
#
# ls.append([88,99])
#
# print("values of ls after append list of values", ls, id(ls))
#
# ls.append(None)
#
# print("values of ls after append None", ls, id(ls))
#
# print("final list after all appends", ls)
#
# ls.extend([66,55]) # extend always takes collection of elements/iterable dt list, str, tuple, dict, set, fs
#
# print("values of ls after extend", ls)
#
# ls.extend("""ETL""")
#
# print("values of ls after extend 'etl automation'", ls)
#
# ls.extend((1,2))
# print("values of ls after extend tuple ", ls)
#
# ls = [1,2]
#
# #Insert
# ls.append([3,4])
# print(ls)
# ls1 = [1,2]
# ls1.extend([3,4])
# print(ls1)

#Inser

# ls = [1,2]
# print("ls is", ls)
# ls.insert(2,'etl')
#
# print("ls after insert", ls)
#
#
# ls.insert(100,'test at 100 index')
#
# print("ls after insert index 100", ls)
#
# print(ls[3])
#
#
# # which is more performant append, insert, extend
#
# #insert
#
# ls.insert(0,'sreeni')
#
# print("ls after append at 0", ls)
#
#
# #index
#
str1 = 'katsreen100@gmail.com'

str1[0:str1.index('@')]

#
# print("position of etl", ls.index('etl'))
# print("position of 1", ls.index(1))
#
#
# ls = [1,1,2,2,2,5,5,6,1]
#
# print("index of 5", ls.index(5))
#
# print("index of 1", ls.index(1,3))
#
# # print('sreeni'.find('1',3,7))
# # print('sreeni'.index('1',3,7))
#
# print("count of 1", ls.count(1))
# print("count of 2", ls.count(2))
# print("count of 5", ls.count(5))
#
#
# # count is available in str
#
# print('sreeni'.count('e'))
#
#
# str1 = 'ETL Automation'
#
# print("count of A", str1.upper().count('A'))


ls = [1,2,3,4,5,6,7,8]


print("ls is", ls)
ls.pop()

print("ls after pop", ls)

ls.pop() # index = -1 last element will be dropped

print("ls after second pop", ls)

ls.pop(0) # index o

print("ls after o index pop", ls)

ls  =[1,1,2,3,4,2]

print("ls is", ls)

ls.remove(2)

print("ls after remove 1", ls)

ls.reverse()

print("ls after reverse", ls)

ls.sort(reverse=True)

print("ls after ", ls)





