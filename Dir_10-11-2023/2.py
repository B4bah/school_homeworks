from functools import lru_cache
from typing import Tuple


def mov(n:int)-> tuple[int, int, int]:
    return n+1, n+3, n*4


@lru_cache(None)
def f(n):
    if any(x >= 59 for x in mov(n)): return 1
    elif all(f(x) == 1 for x in mov(n)): return -1
    elif any(f(x) == -1 for x in mov(n)): return 2
    elif all(f(x) >= 0 for x in mov(n)): return -2
    else: return 0


def f_(n):
    if any(x >= 59 for x in mov(n)): return 1
    elif any(f_(x) == 1 for x in mov(n)): return -1
    elif all(f_(x) == -1 for x in mov(n)): return 2
    elif any(f_(x) == 2 for x in mov(n)): return -2
    else: return 0


for i in range(1, 58):
    if f(i) != 1 and f(i) == -1:
        print('1)', i)
        break

print('2) ', end='')
k = 0
for i in range(1, 58):
    if f(i) != 1 and f(i) == 2:
        k += 1
        print(i, end=' ')
        if k == 2: break
print()

for i in range(1, 58):
    if f_(i) != -1 and f_(i) == -2:
        print('3)', i)
        break

# 1) 14
# 2) 11 13
# 3) 2
