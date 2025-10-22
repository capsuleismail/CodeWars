def squarechecker(number):
    if number == 1:
        return True
    if number < 1:
        return False
    else:
        for i in range(int(number/2)+1):
            if (i*i)==number:
                return True
    return False


def is_square(arr):
    if arr == []:
        return None
    result = list(map(lambda x: squarechecker(x), arr)).count(True)
    return result==len(arr)
