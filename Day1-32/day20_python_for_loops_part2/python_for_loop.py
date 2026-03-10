#syntax
#for iterator_name in collection_type:
    # code


# ls = [1,2,3,4,5,7,6,8,9,10,12,18,21]
# print(" printing all the numbers available in list  using index values")
# print(ls[0])
# print(ls[1])
# print(ls[2])
# print(ls[3])
# print(ls[4])
# print(ls[5])
# print(ls[6])



# ls = (4,8,12)
# # print("printing all the numbers using for loop")
# for i in ls:
#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")
#
# null_check = ['col1','col2', 'col3']
#
# for i in null_check:
#     sql = f"select count(1) from table where {i} is null"
#     print(sql)


# str1 = 'etl automation'
#
#
# # check chara - vowel or consonant
# for i in str1:
#     if i in 'aeiou':
#         print(f"{i} is vowel")
#     else:
#         print(f"{i} is consonant")

# d =1
# a = 2
# t =1
# str1 = 'madam'
# finished_chars=''
# for i in str1:
#     if i not in finished_chars:
#         print(f"count of {i}", str1.count(i))
#         finished_chars = finished_chars +  i

# m2a2d1
str1 = 'madam'
output=''
for i in str1:
    if i not in output:
        cnt = str1.count(i)
        output = output+ i + str(cnt)
print(output)






