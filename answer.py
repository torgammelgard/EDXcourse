def ndigits(x):
    x = abs(x)
    if (x / 10 == 0):
        return 1
    else:
        return 1 + ndigits(x / 10)
