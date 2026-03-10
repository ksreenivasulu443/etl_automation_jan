"""
doc string
"""

# d = {}#dict()
#
# print("d is", d)
# print("d type", type(d))
# print("id is", id(d))
# print("methods available in dict", dir(d))
#
# # d2 = {key:value, key2:value, key3:value}
#
#
#
#
# d.update({5:'Thaman', 6:'Hari', 7:'Yuvaraj'})
#
# print("d is", d)
#
# d3 = {1:'sreeni', 2:'Raghav', 3:'Kavya'}
# print("d3 is", d3)
#
# d3.update({1:'Kattubadi'})
#
# print("d3 after update", d3)
#
# d3.update({1:'sreeni'})
# print("d3 after update", d3) # dictionary will not allow duplicate keys but it allows duplicate values
#
# d3.update({4:['Gokul','A',25]})
#
# print("d3 after update", d3)
#
# print("id after updates", id(d3))


d4 = {}
print("id of d4", d4, id(d4))
d4.update({1:'name'})
print("id of d4 after update", d4, id(d4))

d5 = {}
d6 = {}

print("id d5", id(d5))
print("id d6", id(d6))


d7 = {5:'Thaman', 6:'Hari', 7:'Yuvaraj'}
print("d7 keys", d7.keys(), type(d7.keys()))
print("d7 values", d7.values())
print("d7 items", d7.items())

# get

print("d7.get(5)", d7.get(5))
print("d7.get(7)", d7.get(7))
print("d7.get(0)", d7.get(0))

# fetch the data using indexing

#dict[key]

print("d7[5]", d7[5])
print("d7[6]", d7[6])
print("d7[7]", d7[7])
# print("d7[0]", d7[0])
# d7[6]
# d7[7]

print("d7 is", d7)

# print("d7.pop", d7.pop(5))

print("d7.popitem", d7.popitem())

print("d7 after popitem", d7)

print("d7.popitem", d7.popitem())

print("d7 after popitem", d7)



sampleDict = {"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}

print("sampleDict.get('class')", sampleDict.get('class').get('student').get('marks').get('physics'))
print("sampleDict['class']", sampleDict['class']['student']['marks']['physics'])

d = {'one':'sreeni', True:'hari',1+2j:'sreeni', 1.2:'tim',7:'john', 9:'sreeni',1:'kattu'}
print(d)

# d.pop(5)
# print("d after pop", d)
#
# d.popitem()
# d.popitem()
# print("d after pop", d)







