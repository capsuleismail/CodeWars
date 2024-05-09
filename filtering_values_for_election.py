def average(lst):

    return sum(lst) / len(lst)


def standard_devation(lst):
    a = average(lst)
    st_dv = (sum([(value - a)**2 for value in lst]) / len(lst))
    return st_dv**0.5


def filter_val(lst):
    len_a = len(lst)
    while True:
        avg = average(lst)
        st_d = standard_devation(lst)
        filtered = [data for data in lst if avg -
                    2.5 * st_d <= data <= avg + 2.5 * st_d]
        if filtered == lst:
            break
        else:
            lst = filtered
    len_b = len(lst)
    mean = average(lst)
    st_d = standard_devation(lst)
    return [[len_a, len_b], mean, st_d]


lists = [35, 34, 37, 32, 33, 36, 38, 32, 35, 35, 36, 34, 35, 100, 85, 70]
print(filter_val(lists))
