def quicksort(arr):
    length = len(arr)
    
    if length <= 1:
        return arr
    else:
        
        start = arr[-1]
    
        left = [a for a in arr[:-1] if a <= start]
        right = [a for a in arr[:-1] if a > start]
    
    return quicksort(left) + [start] + quicksort(right)
