from transform_funcs import ReTransform

for x in range(10, 0,  -1):
    num = ReTransform(123, int(f'123{x}4')) + ReTransform(111, int(f'124{x}3'))
    if num % 100 == 0:
        print(int(num / 100))
        break
