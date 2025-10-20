def make_latin_square(n):
    latin_square = []
    
    for i in range(n):
        row = [(j + i) % n + 1 for j in range(n)]
        latin_square.append(row)
    
    return latin_square
