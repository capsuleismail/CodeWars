def rotate_matrix(matrix):
    if not matrix or not matrix[0]:
        return []
    
    n = len(matrix)
    m = len(matrix[0])
    
    transposed = []
    for col in range(m):
        new_row = []
        for row in range(n):
            new_row.append(matrix[row][col])
        transposed.append(new_row)
    
    rotated = transposed[::-1]
    
    return rotated
