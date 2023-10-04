from School_homeworks.Funcs.transform_funcs import retransform

for p in range(1, 101):
    for x in range(10):
        for y in range(10):
            if retransform([8, 9, x, 0], p) + retransform([x, 6, x, 4], p) == retransform([1, y, y, 1, 4], p):
                print(retransform([y, x, y, x], p))
