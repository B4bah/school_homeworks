from School_homeworks.Funcs.divisors_func import divs

k = 0
for num in range(6080068, 6080176+1):
    divs_ = divs(num)
    if len(divs_) == 2:
        k += 1
        print(k, num)

# 1 6080069
# 2 6080131
# 3 6080141
# 4 6080147
# 5 6080149
# 6 6080153
# 7 6080161