# s = set()
#
# print("s is", s)
# print("s type", type(s))
# print("id is", id(s))
# print("methods available in s", dir(s))
#
# s.add(1)
#
#
# print("s after add", s)
#
# s2 = {1,3,4,1,2,6,'etl', 'automation'}
#
# print("s2 is ", s2)

# print(s2[0]) # sets doesnt allow indexing and slicing

# s2.add('etl auto')
#
# print("s2 after add ", s2)

s3 = {1,2,3}
s4 = {3,4,5}

# print("s3.union(s4)", s3.union(s4))
#
#
# print("s3.difference(s4)", s3.difference(s4))
#
# print("s4.difference(s3)", s4.difference(s3))
#
#
#
# print("s3.difference(s4)", s3.difference(s4))
# print("s3 before difference update", s3)
# print("s3.difference_update(s4)", s3.difference_update(s4)) # firstly it performs difference operation and then store o/p back to left side set
#
# print("s3 after difference update", s3)
#
#
# s5 = {7,8,9}
# s6 = {7,8,9,10}
#
# print("s6.difference(s5)",s6.difference(s5))
#
# s6.difference_update(s5)
#
# print("s5", s5)
# print("s6", s6)
#
# s7 ={1,2,3}
# s8 ={3,4,5}
# s9 ={5,6,7}
#
# print(s7.union(s8).union(s9))
#
# print("s7.difference(s8).difference(s9)",s7.difference(s8).difference(s9))
#
# customer ={'cust_id','name','address'}
# transaction ={'cust_id','txn_id','txn_amt'}
# order ={'cust_id','order_id','order_amount',"name"}
#
# print("customer.difference(transaction)", customer.difference(transaction))
#
# print("customer.difference(transaction).difference(order)", customer.difference(transaction).difference(order))
#
#
# customer ={'cust_id','name','address'}
# transaction ={'cust_id','txn_id','txn_amt'}
# order ={'cust_id','order_id','order_amount',"name"}
#
# print("customer.intersection(transaction)", customer.intersection(transaction).intersection(order))
# customer.intersection_update(transaction)
# print("customer after intersection update", customer)
#
#
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
#
# x.update(y)
#
# print(x)



ls1 = [1,2,3,4,4,4,5,5,6] # [1,2,3,4,5,6]

ls2 = ['a','A', 'b', 'b', 'c', 'c'] # ['a', 'A', 'b','c']

s1 = set(ls1)

unique_elements = list(s1)

print("s1", s1)
print("unique_elements", unique_elements)
print("uniq ls2", list(set(ls2)))

s1 = {1,2,3,4}

s2 = frozenset(s1)

print("type of s1", s1,type(s1), dir(s1))
print("type of s2", s2, type(s2), dir(s2))








