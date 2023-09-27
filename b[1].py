from transform_funcs import Transform

summ = 0

for p in range(2, 11):
    if sum(Transform(559, p)) % 2 == 1:
        summ += p

print(summ)
