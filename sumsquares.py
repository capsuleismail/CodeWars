def sumsquares(lst):

    total = 0
    for element in lst:
        if isinstance(element, int):
            total += element * element
        elif isinstance(element, list):
            total = total + sumsquares(element)
    return total
