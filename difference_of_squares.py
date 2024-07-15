def difference_of_squares(n):
    sum_n = n * (n + 1) // 2
    
    square_of_sum = sum_n ** 2
    
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    
    difference = square_of_sum - sum_of_squares
    
    return difference
