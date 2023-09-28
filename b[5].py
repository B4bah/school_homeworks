from transform_funcs import transform, retransform

for x in range(10):
    num = retransform([3, x, 1, 5, x], 15) + retransform([1, 2, 3], int(f'3{x}51')) + x**x + \
          retransform([1, x, 3], int(f'1{x}3')) + retransform([1, x, 2], int(f'{x+1}'))
    if num % 13 == 0:
        print(transform(num, 13))
