def rotate(data, n):

    length = len(data)
    if length == 0:
        return []
    normalize = n % length

    left = data[:length - normalize]
    right = data[length - normalize:]

    return right + left

    return left + right
