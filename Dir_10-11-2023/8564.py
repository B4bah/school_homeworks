from functools import lru_cache


def mov(n: int) -> tuple[int, int, int]:
    return (n - 3, n - 2, n // 4) if n % 4 == 0 else (n - 3, n - 2)


@lru_cache(None)
def f(n: int) -> int:
    if any(x <= 31 for x in mov(n)): return 1
    elif all(f(x) == 1 for x in mov(n)): return -1
    elif any(f(x) == -1 for x in mov(n)): return 2
    elif all(f(x) >= 0 for x in mov(n)): return -2
    else: return 0


def f_(n: int) -> int:
    if any(x <= 31 for x in mov(n)): return 1
    elif any(f_(x) == 1 for x in mov(n)): return -1
    elif any(f_(x) == -1 for x in mov(n)): return 2
    elif any(f_(x) >= 0 for x in mov(n)): return -2
    else: return 0


for i in range(100, 31, -1):
    if f(i) == -1:
        print('1)', i)
        break

for i in range(140, 31, -1):
    if f(i) == 2:
        print('2)', i, end=' ')
        break

for i in range(32, 100):
    if f(i) == 2:
        print(i)
        break

for i in range(32, 101):
    if f(i) == -2:
        print('3)', i)
        break

# 1) 35
# 2) 140 37
# 3) 39
