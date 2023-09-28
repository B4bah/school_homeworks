import itertools as itr

nums = list(itr.product('98432', repeat=10))

k = 0
n = len(nums)
for i in range(len(nums)):
    for j in range(len(nums[i])-1):
        if int(nums[i][j]) % 2 and int(nums[i][j+1]) % 2 == 0 or int(nums[i][j]) % 2 and int(nums[i][j+1]) % 2 != 0:
            k += 1
            break
print(len(nums) - k)