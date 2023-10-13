def divs(num):
    D = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            D.append(num // i)
            D.append(i)
    D = list(sorted(set(D)))
    return D