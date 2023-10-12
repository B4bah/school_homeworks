def digits(num):
    digs= []
    while num > 0:
        digs.append(num % 10)
        num //= 10
    return digs