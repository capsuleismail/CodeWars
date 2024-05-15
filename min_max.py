def min_max(arr):
    min_element = max_element = arr[0]
    
    for num in arr:
        if num < min_element:
            min_element = num
        elif num > max_element:
            max_element = num
    
    return [min_element, max_element]
