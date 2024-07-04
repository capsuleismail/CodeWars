def length_of_sequence(arr, num):
    indices = [i for i, x in enumerate(arr) if x == num]
    
    if len(indices) == 2:
        return indices[1] - indices[0] + 1
    else:
        return 0
