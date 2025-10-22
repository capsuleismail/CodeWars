def index_equals_value(array):
    left = 0
    right = len(array) - 1
    result = -1
    
    
    while left <= right:
        
        mid = (left + right)//2
        
        if array[mid] == mid:

            result = mid
            right = mid - 1
            
        elif array[mid] < mid:
            
            left = mid + 1 
        else:
            right = mid - 1
    
    return result
