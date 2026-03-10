import sys
t = ()  # tuple()
t1 = tuple()


print("values of t", t)
print("type of t", type(t))
print("id of t", id(t))
print("size of t", t.__sizeof__()) # this will not contain GC memmory
print("size of t", sys.getsizeof(t)) # this method includes garbage collectors memory
print("methods of t", dir(t))
print("methods of ls", dir([1,2]))

print("values of t1", t1)
print("type of t1", type(t1))
print("id of t1", id(t1))
print("size of t1", t1.__sizeof__()) # this will not contain GC memmory
print("size of t1", sys.getsizeof(t1)) # this method includes garbage collectors memory
print("methods of t1", dir(t1))


t2 = (1,2)
t3 = (1,2)
print("t2,t3 memory", id(t2), id(t3))
ls1 = [1,2]
ls2 = [1,2]
print("ls1,ls2 memory", id(ls1), id(ls2))

t4 = (1,1.2,1,1+2j, 'etl', [1,2,3,4], True, True,True, False)

print("t4", t4, type(t4), id(t4), dir(t4))

print("coun('etl')", t4.count('etl'))

print("index", t4.index('etl'))


# list & tuple

schema_t = ('name','id','phone') #schema is fixed so better to create it as tuple
schema_l = ['name','id','phone']

print(schema_t,id(schema_t), sys.getsizeof(schema_t), type(schema_t))
print(schema_l,id(schema_l), sys.getsizeof(schema_l), type(schema_l))

import timeit
ls = [1,2,3,4,5,1]
t =  (1,2,3,4,5,1)

print("list", timeit.timeit(stmt=f"{ls}.index(1)", number=1000000))
print("tuple",timeit.timeit(stmt=f"{t}.index(1)",  number=1000000))


customer_data = [1,'sreenivas', 30, 'qa']
customer_data.append('addr')

customer_data = (1,'sreenivas', 30, 'qa')

pkey = ('col1','col2')





