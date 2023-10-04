def transform(num, base):
    digits = []
    while num > 0:
        digits.append(num % base)
        # print(f'{num} % {base} = {num % base}')
        # print(f'{num} //= {base} = {num}')
        num //= base
    # print(f'digits = {digits}')
    return list(reversed(digits))


def retransform(num, base):
    product = 0
    for i in range(len(num)):
        digit = len(num)-i-1
        product += num[digit]*base**i
    #     print(f'product_{digit} = {num[digit]}*{base}**{i} = {num[digit]*base**i}')
    # print(f'product = {product}\n')
    return product

