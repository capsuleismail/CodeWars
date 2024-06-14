def sequence_sum(begin_number, end_number, step):
    total = 0
    for i in range(begin_number, end_number+1, step):
        total += i
    return total
