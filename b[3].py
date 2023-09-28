from transform_funcs import transform

for x in range(100):
    num = transform(5**2026 + 7*5**1013 + 107 - x, 6)
    if num.count(5) == num.count(0) + 28:
        print(x)
        break
