def Transform(num, base):
    digits = []
    while num > 0:
        digits.append(num % base)
        # print(f'{num} % {base} = {num % base}')
        # print(f'{num} //= {base} = {num}')
        num //= base
    # print(f'digits = {digits}')
    return list(reversed(digits))


def ReTransform(num, base):
    product = 0
    nums = [int(digit) for digit in str(num)]
    for i in range(len(nums)):
        digit = len(nums)-i-1
        product += nums[digit]*base**i
    #     print(f'product_{digit} = {nums[digit]}*{base}**{i} = {nums[digit]*base**i}')
    # print(f'product = {product}\n')
    return product

