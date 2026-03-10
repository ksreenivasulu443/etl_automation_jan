# a = 10
# b = 2.0
# c = False
# d = 'etl automation'
# e = 1+2j
# f = None
#
# # list, tuple, dict, set, frozenset
#
# # print("str to list", list(d))
# #
# # print("bool to list", list(c))
#
# l = [(1,'one'),(2,'two')]
# t = ([4,1],[5,7],(6,8))
# d = {1:'Hari', 2:"ganesh","34523":'John'}
# s = {(7,9),(8,1),(9, 10)}
#
# print("list to dict", dict(l))
# # print("set to dict", dict(s))
# print("tuple to dict", dict(t))

# print("float to int", int(b))
# print("bool to int", int(c))
# print("str to int", int(d))
# print("complex to int", int(e))

print("int to float", float(a))
print("bool to float", float(c))
# print("str to float", float(d))
# print("str to int", int(d))
print("complex to float", float(e))

print("int to bool", bool(a))
print("float to bool", bool(b))
print("str to bool", bool(d))
print("complex to bool", bool(e))
print("None to bool", bool(f))

print("int to str", str(a), type(str(a)))
print("float to str", str(b))
print("bool to str", str(c))
print("complex to str", str(e))
print("None to str", str(f))

print("tuple to list", list(t))
print("set to list", list(s))
print("dict to list", list(d))

print("list to tuple", tuple(l))
print("set to tuple", tuple(s))
print("dict to tuple", tuple(d))

# 0, '', None


ls =[5,6,7,12,9,10]
print("ls before sort", ls)
ls.sort(reverse=True)

print("ls after the sort", ls)
rev = ls[::-1]

print("rev", rev)






