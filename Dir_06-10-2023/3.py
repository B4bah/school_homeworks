from School_homeworks.Funcs.divisors_func import divs

k = 0
num = 10_000_000
while True:
    num += 1
    divs_ = divs(num)
    if len(divs_) > 3:
        S = divs_[-2] + divs_[-3]
        if S % 31 == 0 and S < 100_000:
            k += 1
            print(S)
    if k == 5:
        break

# [67270, 50964, 63860, 45074, 21886]