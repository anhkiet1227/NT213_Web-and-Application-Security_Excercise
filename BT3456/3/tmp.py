def xor(x, y):
    return x ^ y


def powsum1(y):
    sum = 0
    for i in range(0, y):
        sum += pow(2, i)
    return sum


def powsum2(y):
    sum = 0
    for i in range(8 - y, 8):
        sum += pow(2, i)
    return sum


def bit1(x, y):
    y = y % 8
    ps = powsum1(y)
    ps = (x & ps) << (8 - y)
    return ps + (x >> y)


def bit2(x, y):
    y = y % 8
    ps = powsum2(y)
    ps = (x & ps) >> (8 - y)
    return (ps + (x << y)) & 0x00ff


def bit(x, y):
    return bit(x, y)


x = 0x8d
y = 0x6c
y = y % 8
print(bit1(x, y))
