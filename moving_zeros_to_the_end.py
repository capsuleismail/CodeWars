def move_zeros(arr):
    not_zero = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[not_zero] = arr[i]
            not_zero += 1
    
    for i in range(not_zero, len(arr)):
        arr[i] = 0
    return arr
