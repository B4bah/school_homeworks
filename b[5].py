from transform_funcs import Transform, ReTransform

for x in range(10):
    num = ReTransform(int(f'3{x}15{x}'), 15) + ReTransform(123, int(f'3{x}51')) + x**x + \
          ReTransform(int(f'1{x}3'), int(f'1{x}3')) + ReTransform(int(f'1{x}2'), int(f'{x+1}'))
    if num % 13 == 0:
        print(Transform(num, 13))
