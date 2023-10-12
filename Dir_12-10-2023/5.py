from School_homeworks.Funcs.digits_func import digits
from School_homeworks.Funcs.is_square_func import is_square

with open('17-294.txt') as f:
    A = [int(x) for x in f.readlines()]
    avg = sum(A) / len(A)
    B = []
    for i in range(len(A)-1):
        sum_digits = sum(digits(A[i])) + sum(digits(A[i + 1]))
        if is_square(sum_digits) and A[i] + A[i+1] > avg:
            B.append(sum_digits)
    print(len(B), max(B))
