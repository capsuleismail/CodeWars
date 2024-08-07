def descending_order(num):
    digits = list(map(int, str(num)))
    digits.sort(reverse=True)
    # Why reverse() is giving problem?
    return int(''.join(list(map(lambda x: str(x), digits))))
