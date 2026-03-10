# ls, str

# tuple, dict,set, fs,

# t = (-8,1,2,3,5,6,-3,-1,0,'123','etl', 'automation')
#
# for i in t:
#     if int(i) >0 :
#         print(f"{i} is positive")
#     elif i < 0:
#         print(f"{i} is negative")
#     else:
#         print(f"{i} is zero or non-numeric ")

s = {1,2,3,4,5}
# l =[1,2,3]
# t =[3,45,5]

# print(sum(s))
# print(sum(l))
# print(sum(t))

# sum_of_elements=0
# for i in s:
#     sum_of_elements = sum_of_elements+i
#
# print("sum_of_elements",sum_of_elements)



# even_sum =0
# odd_sum =0
# for i in s:
#     if i % 2 == 0:
#         even_sum = even_sum + i
#     else:
#         odd_sum = odd_sum + i
#
# print("sum of even", even_sum)
# print("sum of odd", odd_sum)

ls = [1,2,3,4,5,6,8]

even_mul = 1
odd_mul = 1

for i in ls:
    if i % 2 ==0:
        even_mul = even_mul * i
        print('this is even') # 4
    else:
        odd_mul = odd_mul * i
        print('this is odd') # 3
    print("this is out of if-else") #7
#
#
#     print("multiplication of even number", even_mul)
#     print("multiplication of odd number", odd_mul)
#     print('=='*100)


d = {1:10, 2:20, 3:30}

for i in d.keys(): # keys only iterated
    print(i)

for i in d.values():
    print(i)

for key,value in d.items():
    print(key, value)

for i in d:
    print(i)






