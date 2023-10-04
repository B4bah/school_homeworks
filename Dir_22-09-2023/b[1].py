from School_homeworks.Funcs.transform_funcs import transform

summ = 0

for p in range(2, 11):
    if sum(transform(559, p)) % 2 == 1:
        summ += p

print(summ)
