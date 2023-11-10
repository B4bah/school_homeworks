from functools import lru_cache


def mov(t: tuple[int]) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]:
    x = t[0]
    y = t[1]
    return (x + 1, y), (x * 3, y), (x, y + 1), (x, y * 3)


@lru_cache(None)
def f(n):
    if any(sum(x) >= 70 for x in mov(n)):
        return 1
    elif all(f_(x) == 1 for x in mov(n)):
        return -1
    elif any(f(x) == -1 for x in mov(n)):
        return 2
    elif all(f(x) >= 0 for x in mov(n)):
        return -2
    else:
        return 0


def f_(n):
    if any(sum(x) >= 70 for x in mov(n)):
        return 1
    elif any(f(x) == 1 for x in mov(n)):
        return -1
    else:
        return 0


for i in range(1, 63):
    if f_((6, i)) == -1: print('1', i); break

k = 0
for i in range(1, 63):
    if f((6, i)) != 1 and f((6, i)) == 2:
        k += 1
print('2', k)

for i in range(63, 1, -1):
    if f_((6, i)) == -1:
        print('3', i)
        break

# 1 21
# 2 3
# 3 21
