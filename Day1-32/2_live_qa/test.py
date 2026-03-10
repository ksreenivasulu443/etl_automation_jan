a = [1,2]

b = a # reference copy,

print("a details", a, type(a), id(a))

print("b details", b, type(b), id(b))

a.append(10)

print("a details after append", a, type(a), id(a))

print("b details after append", b, type(b), id(b))

b.remove(1)

print("a details after remove", a, type(a), id(a))

print("b details after remove", b, type(b), id(b))


b = b + [10,20]

print(dir(b))


c = [1,2]

d = c.copy()

print("c details", c, type(c), id(c))

print("d details", d, type(d), id(d))

c.append(30)




print("c details after append", c, type(c), id(c))

print("d details after append", d, type(d), id(d))

print(18 // 4) # floor(18/4) ==> floor(4.5)

print(-18//4) # floor(-18/4) ==> floor(-4.5)

