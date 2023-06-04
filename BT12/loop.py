target = 1835996258


def check(value1, value2):
    if value2 <= 1:
        return value1
    if (2*value2) % 3 == 0:
        return check1(value1, value2-1)
    elif (2*value2) % 3 == 1:
        return check2(value1, value2-1)
    else:
        return check3(value1, value2-1)


def check1(value1, value2):
    j = 1
    i = value1
    value1 = j
    while value1 < 100:
        i += value1
        value1 += 1
    return check(i, value2)


def check2(value1, value2):
    if value2 % 2 == 0:
        j = 1
        i = value1
        value1 = j
        while value1 < 1000:
            i += value1
            value1 += 1
        return check(i, value2)
    j = 1
    i = value1
    value1 = j
    while value1 < 1000:
        i -= value1
        value1 += 1
    return check(i, value2)


def check3(value1, value2):
    j = 1
    i = value1
    value1 = j
    while (value1 < 10000):
        i += value1
        value1 += 1
    return check(i, value2)


if __name__ == "__main__":
    for i in range(236492350, 1000000000):
        if (check(i, 99) == target):
            print(i)
            print("Done")
            break

        else:
            print(i)
            continue
    print("END OF PROGRAM")

# 236492408
