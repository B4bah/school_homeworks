from School_homeworks.Funcs.divisors_func import divs

for num in range(193136, 193223+1):
    divs_ = divs(num)
    if len(divs_) == 6:
        print(divs_)

# [1, 5, 25, 7727, 38635, 193175]
# [1, 2, 4, 48299, 96598, 193196]
# [1, 3, 9, 21467, 64401, 193203]
# [1, 7, 49, 3943, 27601, 193207]