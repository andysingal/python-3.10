import math
# def fn_add(a, b):
#     return a + b
#
# def fn_inv(a):
#     return 1/a
#
# def fn_mult(a, b):
#     return a * b
#
# funcs = {fn_add: (10, 20), fn_inv: (2,), fn_mult: (2, 8)}
#
# for f, args in funcs.items():
#     result = f(*args)
#     print(result)
x_coords = (-2, -1, 0, 1, 2)
y_coords = (-2, -1, 0, 1, 2)
grid = [(x, y)
         for x in x_coords
         for y in y_coords]

grid_extended = {(x, y): math.hypot(x, y) for x, y in grid}
