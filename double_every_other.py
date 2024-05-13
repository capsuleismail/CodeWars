def double_every_other(lst):
    while lst:
        for i in range(len(lst)):
            if i % 2 != 0:
                lst[i] *= 2
        return lst
    return None
