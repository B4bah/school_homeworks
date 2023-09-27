from transform_funcs import ReTransform

for p in range(1, 101):
    for x in range(10):
        for y in range(10):
            if ReTransform(int(f'89{x}0'), p) + ReTransform(int(f'{x}6{x}4'), p) == ReTransform(int(f'1{y}{y}14'), p):
                print(ReTransform(int(f'{y}{x}{y}{x}'), p))
