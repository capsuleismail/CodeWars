def small_enough(array, limit):
    return len([i for i in array if i<=limit]) == len(array)
