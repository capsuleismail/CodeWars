def x(n: int) -> list[list[int]]:
    matrix = []
    half = n//2
    
    for i in range(half):
        row = [0] * n
        row[i] = 1
        row[n - 1 - i] = 1
        matrix.append(row)
        
    if n % 2 == 1:
        row = [0] * n
        row[half] = 1
        matrix.append(row)
        
    for i in range(half - 1, -1, -1):
        matrix.append(matrix[i])

    return matrix
