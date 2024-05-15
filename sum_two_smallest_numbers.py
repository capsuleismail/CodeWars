def sum_two_smallest_numbers(arr):
    
    if len(arr) < 4:
        return None
    
    smallest = float('inf')
    second_smallest = float('inf')
     
    for i in range(len(arr)):
        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]
        elif arr[i] < second_smallest and arr[i] != smallest:
            second_smallest = arr[i]
    
    return smallest+second_smallest
