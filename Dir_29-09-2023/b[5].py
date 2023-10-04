import itertools as itr

nums = [num for num in list(itr.product('0123456', repeat=7))
        if num[0] not in ('3', '5') and '22' and '44' not in ''.join(num)]

print(len(nums))