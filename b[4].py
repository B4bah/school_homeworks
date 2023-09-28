from transform_funcs import retransform

for x in range(10, 0,  -1):
    num = retransform([1, 2, 3], int(f'123{x}4')) + retransform([1, 1, 1], int(f'124{x}3'))
    if num % 100 == 0:
        print(int(num / 100))
        break
