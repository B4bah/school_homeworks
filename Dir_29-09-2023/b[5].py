import itertools as itr

nums = [num for num in list(itr.product('0123456', repeat=7))
        if not (num[0] in ('0', '3', '5')) and not ('22' in ''.join(num) and '44' in ''.join(num))]

print(len(nums))