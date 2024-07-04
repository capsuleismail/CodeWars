def determine_winner(board):
    black_count = 0
    white_count = 0
    
    for row in board:
        black_count += row.count("B")
        white_count += row.count("W")
    
    if black_count > white_count:
        return ("B", black_count)
    elif white_count > black_count:
        return ("W", white_count)
    else:
        return ("T", black_count) 
