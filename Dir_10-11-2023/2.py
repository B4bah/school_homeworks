from functools import lru_cache
from icecream import ic


def mov(n: int) -> tuple[int, int, int]:
    return n+1, n+3, n*4


@lru_cache(None)
def f(n: int) -> int:
    if any(x >= 59 for x in mov(n)): return 1
    elif all(f(x) == 1 for x in mov(n)): return -1
    elif any(f(x) == -1 for x in mov(n)): return 2
    elif all(f(x) >= 0 for x in mov(n)): return -2
    else: return 0


def f_(n: int) -> int:
    if any(x >= 59 for x in mov(n)): return 1
    elif any(f_(x) == 1 for x in mov(n)): return -1
    elif all(f_(x) == -1 for x in mov(n)): return 2
    elif any(f_(x) >= 0 for x in mov(n)): return -2
    else: return 0


for i in range(1, 58):

    if f(i) == -1:
        ic('1)', i)
        break

# print('2) ', end='')
# k = 0
# for i in range(1, 58):
#     if f(i) == 2:
#         k += 1
#         print(i, end=' ')
#         if k == 2: break
# print()

k = 0
for i in range(1, 58):
    if f(i) == 2:
        k += 1
        ic('2) ', i)
        if k == 2: break


for i in range(1, 58):
    if f_(i) == -2:
        ic('3)', i)
        break

# 1) 14
# 2) 11 13
# 3) 2
