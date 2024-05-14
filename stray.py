def stray(arr):
    result = 0
    for i in range(len(arr)):
        result ^= arr[i]
    return result
