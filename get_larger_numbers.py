def get_larger_numbers(a, b):
    result = []
    for i in range(0, len(a)):
        if a[i] > b[i]:
            result.append(a[i])
        else:
            result.append(b[i])
    return result
