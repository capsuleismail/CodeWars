def sort_array(A):
    odd_numbers = [num for num in A if num % 2 != 0]
    
    odd_numbers.sort()
    
    odd_iter = iter(odd_numbers)
    
    sorted_array = [next(odd_iter) if num % 2 != 0 else num for num in A]
    
    return sorted_array
