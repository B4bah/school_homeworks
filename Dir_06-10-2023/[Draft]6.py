k = 0
x = 0
while k < 5:
    for y in '0123456789':
        num_1 = int(f'{x}0{y}{y}3{x}')
        num_2 = int(f'{x}4{y}{y}2')
        num_3 = int(f'{x}1{x}')
        if num_1 > 700_000 and num_2 > 700_000 and num_3 > 700_000:
            if not (num_1 % 13 == 0) and not (num_2 % 13 == 0) and \
                    not (num_3 % 13 == 0):
                x += 1
