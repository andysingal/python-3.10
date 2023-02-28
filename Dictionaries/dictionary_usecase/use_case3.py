a = {'k1': 100, 'k2': 200}

# def fn_add(a, b):
#     return a + b
#
# def fn_inv(a):
#     return 1/a
#
# def fn_mult(a, b):
#     return a * b
#
# funcs = {fn_add: (10,20),fn_inv:(2,),fn_mult: (2,8)}
#
# for f, args in funcs.items():
#     result = f(*args)
#     print(result)

# keys = ['a', 'b', 'c']
# values = (1, 2, 3)
#
# d = {}  # creates an empty dictionary
# for k, v in zip(keys, values):
#     d[k] = v
#
# #d = {k: v for k, v in zip(keys, values)}
# print(d)
# import math
# x_coords = (-2, -1, 0, 1, 2)
# y_coords = (-2, -1, 0, 1, 2)
#
# grid = [(x,y)
#         for x in x_coords
#         for y in y_coords]
#
# grid_extended = {(x, y): math.hypot(x, y) for x, y in grid}
# print(grid_extended)

# counters = dict.fromkeys(['a', 'b', 'c'], 0)
# print(counters)

d = dict(zip('abc', range(1, 4)))
print(d)


