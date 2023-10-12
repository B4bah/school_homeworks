from School_homeworks.Funcs.digits_func import digits

with open('17-304.txt') as f:
    A = [int(x) for x in f.readlines()]
    B = []
    for i in range(len(A)-1):
        num = min(x for x in A if x % 121 == 0)
        sum_digits = sum(x for x in digits(A[i]) if x % 2 == 0)
        sum_digits_ = sum(x for x in digits(A[i]) if x % 2 != 0)
        if sum_digits_ > sum_digits and A[i] + A[i+1] % num != 0:
            B.append(A[i] + A[i+1])
    print(len(B), max(B))