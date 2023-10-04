from School_homeworks.Funcs.transform_funcs import transform

num = transform(49**129 + 7**131 - 2, 7)
num = [max(num) for i in range(len(num)) if num[i] == 0]

print(num.count(max(num)))
