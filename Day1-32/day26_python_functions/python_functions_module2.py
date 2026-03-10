# def calc(a,b): # a, b parameters
#     print(f"a is {a} and b is {b}")
#     return a+b
# # #
# print(calc(10,12)) # 10,12 are positional arguments
# # #
# print(calc(a=5,b=7)) # a=5, b=7 are keyword arguments
# # #
# print(calc(b=7,10)) # we should pass positional arguments after keyword
# # #
# print(calc(10,b=20)) # 10 is positional arg & b=20 is keyword
#
#
# def calc(a, b,c=0): # firstly pass all parameters then default
#     print("a value is ", a)
#     print("b value is ", b)
#     print("c value is ", c)
#     return a+b+c
# #
# #
# print(calc(10,20)) #10,20 positional
# print(calc(10,20,15))
#
# print(calc(10,b=20,c=15))

# def calc(a, b,c=0,d=0,e=0,f=0): # firstly pass all parameters then default
#     print("a value is ", a)
#     print("b value is ", b)
#     print("c value is ", c)
#     print("d value is ", d)
#     return a+b+c+d+e+f
#
# calc(10,20,50,60,49,89,89,45)

# def calc(*abc): # args - positional variable length arguments
#     print(abc, type(abc))
#     square_sum = 0
#     for i in args:
#         square_sum += i*i
#     return square_sum
#
#
# print(calc(1,2,3))
#
# print(calc(1,2,3,4))
#
# output3 = calc(1,2,3,4,5)

# print(output)
#
# print(calc(4,5))
#
# print(calc(4,5,6))
# print(calc(4,5,6,7))

def calc(**sreeni): # kwargs - keyword variable length arguments
    print(sreeni, type(sreeni), sum(sreeni.values()))
    all_sum = 0
    for i in sreeni.values():
        all_sum = all_sum + i
    return all_sum


print(calc(a=10,b=20, x=5, y=4, k = 2))

# calc(l=9, m=10)



